import psutil
import os
import sys
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def force_close_apps():
    # List of critical Windows processes to exclude
    protected_processes = [
        'explorer.exe', 'svchost.exe', 'csrss.exe', 'winlogon.exe', 
        'services.exe', 'lsass.exe', 'smss.exe', 'wininit.exe',
        'System', 'Registry', 'fontdrvhost.exe'
    ]
    
    closed_count = 0
    
    print("Starting to close applications...")
    
    # Iterate through all running processes
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            process_name = proc.info['name'].lower()
            
            # Skip if process is in protected list
            if process_name in protected_processes:
                continue
                
            # Skip system processes
            if proc.pid < 100:
                continue
                
            # Attempt to terminate the process
            process = psutil.Process(proc.pid)
            process.terminate()
            closed_count += 1
            print(f"Closed: {process_name}")
            
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    
    print(f"\nCompleted! Closed {closed_count} applications.")

if __name__ == "__main__":
    # Check if running with admin privileges
    if not is_admin():
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    else:
        # Run the main function
        force_close_apps()