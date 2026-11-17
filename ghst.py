import time
import serial
import serial.tools.list_ports
import sys
from rich.console import Console

console = Console()

def find_esp_port():
    target_keywords = ["CP210", "CH34", "FTDI", "USB-SERIAL", "UART", "Silicon Labs"]
    
    with console.status("[bold green]Scanning system for unsecure ports...[/bold green]", spinner="dots"):
        time.sleep(1.5)  # Quick visual buffer for the animation
        ports = serial.tools.list_ports.comports()
    
    for port in ports:
        description = port.description.upper()
        if any(keyword.upper() in description for keyword in target_keywords):
            console.print(f"[bold green][+][/bold green] Initializing secure line to ghost_bw16: [cyan]{port.device}[/cyan] ({port.description})")
            return port.device
            
    for port in ports:
        if "USB" in port.device.upper() or "COM" in port.device.upper():
            console.print(f"[bold yellow][!][/bold yellow] Warning: No explicit chip match. Falling back to: [cyan]{port.device}[/cyan]")
            return port.device

    return None

# --- Main Implementation ---
SERIAL_PORT = find_esp_port()
BAUD_RATE = 115200 

if not SERIAL_PORT:
    console.print("[bold red][-] Error: No plugged-in ESP or Serial devices detected. Check your USB cable![/bold red]")
    sys.exit(1)

try:
    with console.status(f"[bold green]Initializing serial interface on {SERIAL_PORT}...[/bold green]", spinner="dots"):
        bw16 = serial.Serial(port=SERIAL_PORT, baudrate=BAUD_RATE, timeout=0.1)
        time.sleep(0.5)
        
    console.print(f"[bold blue][+][/bold blue] Connection SUCCESSFUL: [cyan]{SERIAL_PORT}[/cyan] at [yellow]{BAUD_RATE}[/yellow] baud.")
    console.print("[bold gray]CMD: 'scan' to commence RECON | CMD: 'help' for available commands | CMD: 'EXIT' to quit.[/bold gray]\n")

    while True:
        user_command = input("UNKNWN -> ghost_bw16: ").strip()
        
        if user_command.upper() == "EXIT":
            break
            
        if user_command:
            payload = f"{user_command}\r\n".encode('utf-8')
            bw16.write(payload)
            
            is_scan_cmd = "SCAN" in user_command.upper() or "LAP" in user_command.upper()
            status_msg = "[bold violet]Performing radio scan... Please wait.[/bold violet]" if is_scan_cmd else f"[bold fuchsia]Awaiting response for '{user_command}'...[/bold fuchsia]"
            
            # Print the header immediately so the stream outputs sequentially underneath it
            console.print("[bold red]ghost Response:[/bold red]")
            
            with console.status(status_msg, spinner="dots"):
                # Structural wait for the very first line to hit the UART bridge
                time.sleep(0.1)
                
                has_response = False
                consecutive_empty_reads = 0
                
                # Streaming loop: We print lines instantly as they trickle in
                while True:
                    line = bw16.readline().decode('utf-8', errors='ignore')
                    
                    if line:
                        consecutive_empty_reads = 0  # Reset timeout counter if data flows
                        clean_line = line.strip()
                        if clean_line:
                            # Print immediately so the user can watch the scan results stream in live
                            console.print(f"  [green]{clean_line}[/green]")
                            has_response = True
                    else:
                        consecutive_empty_reads += 1
                    
                    # DYNAMIC TIMEOUT BARRIER:
                    # If it's a scan command, we give the chip up to 6.0 seconds (60 timeouts * 0.1s)
                    # of TOTAL SILENCE to hop 2.4/5GHz channels before giving up.
                    # For normal commands, we only allow 0.4 seconds of silence.
                    max_silence_limit = 60 if is_scan_cmd else 20
                    
                    if consecutive_empty_reads >= max_silence_limit:
                        break
            
            if not has_response:
                console.print("  [bold red][No response received from chip. Check connection or baud rate.][/bold red]")
            print()  # Visual spacer line


                    
except serial.SerialException as e:
    console.print(f"[bold red][-] Error opening port {SERIAL_PORT}: {e}[/bold red]")
finally:
    if 'bw16' in locals() and bw16.is_open:
        bw16.close()
        console.print("\n[bold blue]Disconnected.[/bold blue] 👋")
