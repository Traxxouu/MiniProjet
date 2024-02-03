import tkinter as tk
import subprocess
import re

def retrieve_password():
    selected_item = ssid_listbox.curselection()
    if selected_item:
        ssid = ssid_listbox.get(selected_item)
        try:
            result = subprocess.run(['netsh', 'wlan', 'show', 'profile', ssid, 'key=clear'], capture_output=True, text=True)
            password = extract_password(result.stdout)
            open_password_window(ssid, password)
        except subprocess.CalledProcessError as e:
            open_password_window(ssid, f"Error: {e}")

def extract_password(output):
    key_content_pattern = re.compile(r"Contenu de la cl‚\s+:\s(.+)")
    matches = key_content_pattern.search(output)
    if matches:
        password = matches.group(1)
        return password.strip()
    return "Le mot de passe n'est pas retrouvé ❌"

def open_password_window(ssid, password):
    password_window = tk.Toplevel(root)
    password_window.title(f"Mot de passe pour : {ssid}")
    password_label = tk.Label(password_window, text=f"Mot de passe pour {ssid} : {password}")
    password_label.pack(padx=20, pady=20)


root = tk.Tk()
root.title("Wifind")


ssid_label = tk.Label(root, text="Clique sur un réseaux 🌐 pour obtenir son mot de passe 🔑")
ssid_listbox = tk.Listbox(root)
retrieve_button = tk.Button(root, text="Retrouve ton mot de passe 🔎", command=retrieve_password)
text = tk.Label(root, text="By Maël")


ssid_label.grid(row=0, column=0, padx=10, pady=10)
ssid_listbox.grid(row=1, column=0, padx=10, pady=10)
retrieve_button.grid(row=2, column=0, padx=10, pady=10)
text.grid(row=3, column=0, padx=10, pady=10)




result = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True)
ssids = [line.split(":")[1].strip() for line in result.stdout.splitlines() if "Tous les utilisateurs" in line]
for ssid in ssids:
    ssid_listbox.insert(tk.END, ssid)


root.mainloop()




