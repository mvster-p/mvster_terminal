# AirCLI

**Airgeddon-style CLI WiFi Auditor for Kali Linux**

Pure command-line, no graphics, text colored by mode/step (SCAN, CAPTURE, EVIL, CAPTIVE, etc).

Implements core airgeddon functionality + enhanced **Fake AP + Captive Portal** feature.

Default captive portal = "Wi-Fi Security Update" page that asks users to enter WiFi credentials.

## Features (like airgeddon, graphics-free)

- Interface management (select + monitor/managed mode)
- WiFi network scanning (airodump-ng)
- Target selection (auto or manual)
- WPA handshake capture (with assisted deauth)
- Deauthentication / DoS attacks
- Handshake verification + offline cracking (aircrack-ng + wordlist)
- **Fake Access Point** (standalone rogue AP)
- **Evil Twin + Captive Portal** (highly featured)
  - Choose custom name (ESSID), channel, optional BSSID spoof
  - Clones current target or fully manual
  - Uses hostapd + dnsmasq
  - DNS blackhole + HTTP/HTTPS->local redirect (captive)
  - Real-time credential capture logging to terminal + file
  - Default portal: convincing "Wi-Fi Security Update" login page
  - While running: option to deauth clients + view captured creds

## Requirements (Kali Linux recommended)

```bash
sudo apt update
sudo apt install -y aircrack-ng hostapd dnsmasq iw net-tools iptables python3
```

Optional but useful:
```bash
sudo apt install -y macchanger wordlists
```

## Install & Run

```bash
cd /home/p/aircli
chmod +x aircli.py
sudo python3 aircli.py
```

Or copy to PATH:
```bash
sudo cp aircli.py /usr/local/bin/aircli
sudo chmod +x /usr/local/bin/aircli
sudo aircli
```

Run **as root** (or with sudo) — required for monitor mode, hostapd, iptables, raw sockets.

## Quick Example Flow (Evil Twin + Captive)

1. Start `sudo python3 aircli.py`
2. **1** → Interface Management → pick your wlan interface
3. **3** → Enable MONITOR mode
4. **2** → Network Discovery → scan and select a target (or skip)
5. **5** → Fake AP + Evil Twin + Captive Portal
   - Choose **2** for Evil Twin + Captive
   - Clone target or enter custom name + channel
6. AP comes up + portal running
7. (Optional) Send deauths from the sub-menu to force clients off the real AP onto yours
8. Watch for captured credentials in the terminal (also saved to `/tmp/aircli_captured_creds.txt`)

Stop with option **3** in the Fake AP menu or main **6** Cleanup.

## Captive Portal Details

- **Default page**: "Wi-Fi Security Update" (firmware patch story)
- Form asks for:
  - Network SSID (pre-filled, read-only)
  - Wi-Fi Password
- On submit: credentials logged with timestamp + client IP
- Victim sees "Update Complete" success page
- All DNS points to the attacker (blackhole)
- Port 80 + 443 redirected to the portal

You can extend the HTML by editing the `CAPTIVE_HTML` constant inside `aircli.py`.

## Important Notes

- **Legal/ethical use only.** Only test networks you own or are authorized to audit.
- Some modern clients (iOS, Android, Windows) are aggressive about captive portals and saved WPA profiles. Deauth + open evil twin is the classic technique.
- Full 5 GHz / VIF / advanced enterprise / WPS / PMKID with hcxdumptool are possible future additions. Current focus is core + excellent FakeAP+Captive.
- Cleanup restores interfaces and flushes iptables on exit or via menu option 6.
- Works best with external USB WiFi adapter that supports monitor + AP mode (e.g. Alfa cards with good chipsets).

## Coloring

Every important message is prefixed and colored according to the step:

- `[SCAN]` blue
- `[CAPTURE]` yellow
- `[DEAUTH]` / `[ATTACK]` red
- `[EVIL]` purple
- `[CAPTIVE]` bright magenta/purple
- `[TARGET]` / success green
- etc.

## Credits / Inspiration

Inspired by airgeddon (https://github.com/v1s1t0r1sh3r3/airgeddon) by v1s1t0r1sh3r3.

This is a new independent CLI implementation focused on being lightweight, scriptable, and graphics-free while delivering the key attack workflows.

## License

For educational and authorized security testing use only. Use responsibly.