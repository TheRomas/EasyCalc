import tkinter as tk
from tkinter import ttk

def calcular_consumo(distancia, combustivel):
    return distancia / combustivel

def listar_veiculos():
    return {
        "Carro compacto": 14,
        "Carro sedan": 12,
        "SUV": 9,
        "Caminhonete": 8,
        "Moto": 30
    }

class AplicativoConsumo(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculador de Consumo de Combustível")
        self.geometry("500x400")

        self.veiculos = listar_veiculos()

        # Criação dos widgets
        self.criar_widgets()

    def criar_widgets(self):
        # Dropdown para seleção de veículo
        ttk.Label(self, text="Selecione o veículo:").pack(pady=5)
        self.veiculo_var = tk.StringVar()
        self.veiculo_dropdown = ttk.Combobox(self, textvariable=self.veiculo_var)
        self.veiculo_dropdown['values'] = list(self.veiculos.keys()) + ["Personalizado"]
        self.veiculo_dropdown.pack(pady=5)
        self.veiculo_dropdown.bind("<<ComboboxSelected>>", self.on_veiculo_select)

        # Entrada para distância
        ttk.Label(self, text="Distância percorrida (km):").pack(pady=5)
        self.distancia_entry = ttk.Entry(self)
        self.distancia_entry.pack(pady=5)

        # Entrada para combustível (inicialmente oculta)
        self.combustivel_label = ttk.Label(self, text="Combustível usado (l):")
        self.combustivel_entry = ttk.Entry(self)

        # Botão de cálculo
        self.calcular_button = ttk.Button(self, text="Calcular", command=self.calcular)
        self.calcular_button.pack(pady=20)

        # Label para exibir resultado
        self.resultado_label = ttk.Label(self, text="")
        self.resultado_label.pack(pady=10)

    def on_veiculo_select(self, event):
        if self.veiculo_var.get() == "Personalizado":
            self.combustivel_label.pack(pady=5)
            self.combustivel_entry.pack(pady=5)
        else:
            self.combustivel_label.pack_forget()
            self.combustivel_entry.pack_forget()

    def calcular(self):
        try:
            distancia = float(self.distancia_entry.get())
            veiculo = self.veiculo_var.get()

            if veiculo == "Personalizado":
                combustivel = float(self.combustivel_entry.get())
                consumo = calcular_consumo(distancia, combustivel)
                resultado = f"Consumo: {consumo:.2f} km/l"
            elif veiculo in self.veiculos:
                consumo = self.veiculos[veiculo]
                combustivel = distancia / consumo
                resultado = f"Combustível gasto: {combustivel:.2f} litros"
            else:
                raise ValueError("Veículo não selecionado")

            self.resultado_label.config(text=resultado)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

if __name__ == "__main__":
    app = AplicativoConsumo()
    app.mainloop()



