import tkinter as tk

class Agenda:
    def __init__(self, master):
        self.master = master
        master.title("Agenda")

        # Créer une liste pour stocker les événements
        self.events = {}

        # Créer un widget de texte pour afficher les événements
        self.event_display = tk.Text(master, height=10, width=50)
        self.event_display.pack()

        # Créer un widget de saisie pour ajouter un événement
        self.event_entry = tk.Entry(master)
        self.event_entry.pack()

        # Créer un widget de bouton pour ajouter l'événement
        self.add_button = tk.Button(master, text="Ajouter", command=self.add_event)
        self.add_button.pack()

    def add_event(self):
        # Récupérer la saisie de l'utilisateur
        event = self.event_entry.get()

        # Ajouter l'événement au dictionnaire des événements
        self.events.setdefault(tk.StringVar().get(), []).append(event)

        # Effacer le champ de saisie
        self.event_entry.delete(0, tk.END)

        # Mettre à jour l'affichage des événements
        self.update_event_display()

    def update_event_display(self):
        # Effacer le contenu précédent du widget de texte
        self.event_display.delete(1.0, tk.END)

        # Afficher les événements dans le widget de texte
        for day, events in self.events.items():
            self.event_display.insert(tk.END, day + ":\n")
            for event in events:
                self.event_display.insert(tk.END, "\t- " + event + "\n")

root = tk.Tk()
my_agenda = Agenda(root)
root.mainloop()