#!/usr/bin/env python3
"""Roof measurement + proposal helper.

Collects customer information, geocodes an address, downloads a map image,
then generates a PDF-ready proposal report.
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import requests
from fpdf import FPDF

USER_AGENT = "roof-proposal-tool/1.0 (+https://example.local)"


@dataclass
class ClientInfo:
    name: str
    address: str
    phone: str
    email: str
    repair_summary: str


@dataclass
class RoofMetrics:
    roof_sq_ft: float
    pipes: int
    drains: int
    chimneys: int
    skylights: int
    hvac_units: int


def prompt(label: str, required: bool = True) -> str:
    while True:
        value = input(f"{label}: ").strip()
        if value or not required:
            return value
        print("This field is required.")


def prompt_float(label: str) -> float:
    while True:
        value = prompt(label)
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number.")


def prompt_int(label: str) -> int:
    while True:
        value = prompt(label)
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid integer.")


def geocode_address(address: str) -> tuple[Optional[float], Optional[float]]:
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": address, "format": "json", "limit": 1}
    headers = {"User-Agent": USER_AGENT}
    response = requests.get(url, params=params, headers=headers, timeout=20)
    response.raise_for_status()
    data = response.json()
    if not data:
        return None, None
    return float(data[0]["lat"]), float(data[0]["lon"])


def download_map_image(
    address: str,
    lat: float,
    lon: float,
    output_dir: Path,
    provider: str,
) -> Optional[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    image_path = output_dir / "roof_view.png"

    if provider == "google":
        api_key = os.getenv("GOOGLE_MAPS_API_KEY")
        if not api_key:
            print("GOOGLE_MAPS_API_KEY not found. Falling back to OpenStreetMap.")
            provider = "osm"
        else:
            url = "https://maps.googleapis.com/maps/api/staticmap"
            params = {
                "center": f"{lat},{lon}",
                "zoom": 20,
                "size": "1280x1280",
                "maptype": "satellite",
                "markers": f"color:red|{lat},{lon}",
                "key": api_key,
            }
            res = requests.get(url, params=params, timeout=30)
            res.raise_for_status()
            image_path.write_bytes(res.content)
            return image_path

    if provider == "osm":
        url = "https://staticmap.openstreetmap.de/staticmap.php"
        params = {
            "center": f"{lat},{lon}",
            "zoom": 19,
            "size": "1024x1024",
            "markers": f"{lat},{lon},red-pushpin",
        }
        res = requests.get(url, params=params, timeout=30)
        res.raise_for_status()
        image_path.write_bytes(res.content)
        return image_path

    print(f"Unsupported provider '{provider}'.")
    return None


def collect_data() -> tuple[ClientInfo, RoofMetrics, str, str]:
    print("\n=== Client Details ===")
    client = ClientInfo(
        name=prompt("Client name"),
        address=prompt("Property address"),
        phone=prompt("Phone"),
        email=prompt("Email"),
        repair_summary=prompt("Summary of repairs needed"),
    )

    print("\n=== Roof Metrics ===")
    print("Enter measured/observed values. (Use satellite image as a visual aid.)")
    roof = RoofMetrics(
        roof_sq_ft=prompt_float("Roof area (sq ft)"),
        pipes=prompt_int("Pipe penetrations count"),
        drains=prompt_int("Roof drains count"),
        chimneys=prompt_int("Chimneys count"),
        skylights=prompt_int("Skylights count"),
        hvac_units=prompt_int("HVAC curb/unit count"),
    )

    logo_path = prompt("Company logo path (optional)", required=False)
    provider = prompt("Map provider [osm/google]", required=False).lower() or "osm"

    return client, roof, logo_path, provider


def create_pdf_report(
    report_path: Path,
    client: ClientInfo,
    roof: RoofMetrics,
    map_image_path: Optional[Path],
    logo_path: Optional[str],
    lat: Optional[float],
    lon: Optional[float],
) -> None:
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    if logo_path and Path(logo_path).exists():
        pdf.image(logo_path, x=10, y=8, w=35)
        pdf.ln(20)

    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "Roof Inspection & Proposal Report", ln=True)

    pdf.set_font("Helvetica", "", 11)
    pdf.cell(0, 8, f"Generated: {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=True)
    pdf.ln(2)

    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 8, "Client Information", ln=True)
    pdf.set_font("Helvetica", "", 11)
    pdf.multi_cell(0, 7, (
        f"Name: {client.name}\n"
        f"Address: {client.address}\n"
        f"Phone: {client.phone}\n"
        f"Email: {client.email}"
    ))

    if lat is not None and lon is not None:
        pdf.cell(0, 7, f"Coordinates: {lat:.6f}, {lon:.6f}", ln=True)

    pdf.ln(2)
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 8, "Requested Repairs", ln=True)
    pdf.set_font("Helvetica", "", 11)
    pdf.multi_cell(0, 7, client.repair_summary)

    pdf.ln(2)
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 8, "Roof Measurements & Features", ln=True)
    pdf.set_font("Helvetica", "", 11)
    measurements = (
        f"Estimated roof area: {roof.roof_sq_ft:,.2f} sq ft\n"
        f"Pipes: {roof.pipes}\n"
        f"Drains: {roof.drains}\n"
        f"Chimneys: {roof.chimneys}\n"
        f"Skylights: {roof.skylights}\n"
        f"HVAC units: {roof.hvac_units}"
    )
    pdf.multi_cell(0, 7, measurements)

    if map_image_path and map_image_path.exists():
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 12)
        pdf.cell(0, 10, "Property Overhead View", ln=True)
        pdf.image(str(map_image_path), x=10, y=25, w=190)
        pdf.set_y(220)
        pdf.set_font("Helvetica", "", 9)
        pdf.multi_cell(
            0,
            5,
            "Note: For true satellite imagery, use provider 'google' with GOOGLE_MAPS_API_KEY, "
            "or integrate EagleView/other commercial APIs. OSM mode is a map image aid.",
        )

    pdf.output(str(report_path))


def main() -> None:
    parser = argparse.ArgumentParser(description="Roof proposal report helper")
    parser.add_argument(
        "--output-dir",
        default="output",
        help="Directory where report files are saved (default: output)",
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    client, roof, logo_path, provider = collect_data()

    print("\nGeocoding address...")
    lat = lon = None
    try:
        lat, lon = geocode_address(client.address)
        if lat is None or lon is None:
            print("Address not found. Continuing without map coordinates.")
    except requests.RequestException as exc:
        print(f"Could not geocode address: {exc}")

    map_path = None
    if lat is not None and lon is not None:
        print(f"Downloading map image using '{provider}'...")
        try:
            map_path = download_map_image(client.address, lat, lon, output_dir, provider)
        except requests.RequestException as exc:
            print(f"Could not download map image: {exc}")

    report_name = f"roof_report_{dt.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    report_path = output_dir / report_name
    create_pdf_report(report_path, client, roof, map_path, logo_path, lat, lon)

    print(f"\nDone. PDF report created: {report_path}")
    if map_path:
        print(f"Map image saved: {map_path}")


if __name__ == "__main__":
    main()
