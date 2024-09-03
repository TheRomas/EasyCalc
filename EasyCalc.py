import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk

def calcular_consumo(distancia, consumo):
    return distancia / consumo

class AplicativoConsumo(ThemedTk):
    def __init__(self):
        super().__init__(theme="equilux")

        self.title("EASYCALC - Consumo de Combustível")
        self.geometry("800x600")
        self.configure(bg='#2E2E2E')

        self.carros_compactos = {
            "Renault Kwid 1.0": {
                "Eficiência": 1.36,
                "Cidade (etanol)": 10.8,
                "Estrada (etanol)": 11.0,
                "Cidade (gasolina)": 15.3,
                "Estrada (gasolina)": 15.7,
                "Preço": 71190.00
            },
            "Chevrolet Onix Plus 1.0": {
                "Eficiência": 1.42,
                "Cidade (etanol)": 9.3,
                "Estrada (etanol)": 12.0,
                "Cidade (gasolina)": 13.5,
                "Estrada (gasolina)": 17.4,
                "Preço": 97390.00
            },
            "Chevrolet Onix 1.0": {
                "Eficiência": 1.46,
                "Cidade (etanol)": 9.3,
                "Estrada (etanol)": 11.4,
                "Cidade (gasolina)": 13.3,
                "Estrada (gasolina)": 16.5,
                "Preço": 86150.00
            },
            "Peugeot 208 1.0": {
                "Eficiência": 1.47,
                "Cidade (etanol)": 9.6,
                "Estrada (etanol)": 11.1,
                "Cidade (gasolina)": 13.3,
                "Estrada (gasolina)": 15.8,
                "Preço": 91990.00
            },
            "Fiat Cronos 1.0": {
                "Eficiência": 1.47,
                "Cidade (etanol)": 9.8,
                "Estrada (etanol)": 11.0,
                "Cidade (gasolina)": 13.4,
                "Estrada (gasolina)": 15.6,
                "Preço": 93990.00
            },
            "Renault Stepway 1.0": {
                "Eficiência": 1.48,
                "Cidade (etanol)": 10.0,
                "Estrada (etanol)": 10.2,
                "Cidade (gasolina)": 13.9,
                "Estrada (gasolina)": 14.7,
                "Preço": 84470.00
            },
            "Volkswagen Polo 1.0T": {
                "Eficiência": 1.48,
                "Cidade (etanol)": 9.3,
                "Estrada (etanol)": 10.5,
                "Cidade (gasolina)": 13.5,
                "Estrada (gasolina)": 15.0,
                "Preço": 87990.00
            },
            "Fiat Mobi": {
                "Eficiência": 1.50,
                "Cidade (etanol)": 9.6,
                "Estrada (etanol)": 10.4,
                "Cidade (gasolina)": 13.5,
                "Estrada (gasolina)": 15.0,
                "Preço": 72990.00
            },
            "Hyundai HB20 1.0": {
                "Eficiência": 1.51,
                "Cidade (etanol)": 9.6,
                "Estrada (etanol)": 10.4,
                "Cidade (gasolina)": 13.5,
                "Estrada (gasolina)": 14.6,
                "Preço": 82290.00
            },
            "Volkswagen Polo 1.0": {
                "Eficiência": 1.51,
                "Cidade (etanol)": 9.3,
                "Estrada (etanol)": 10.5,
                "Cidade (gasolina)": 13.5,
                "Estrada (gasolina)": 15.0,
                "Preço": 87990.00
            }
        }

        self.criar_widgets()

    def criar_widgets(self):
        style = ttk.Style(self)
        style.configure('TLabel', background='#2E2E2E', foreground='#FF6600', font=('Roboto', 12))
        style.configure('TButton', font=('Roboto', 12), background='#FF6600', foreground='#2E2E2E')
        style.configure('TEntry', font=('Roboto', 12))
        style.configure('TCombobox', font=('Roboto', 12))

        # Título
        titulo = ttk.Label(self, text="EASYCALC", font=('Roboto', 28, 'bold'), foreground='#FF6600')
        titulo.pack(pady=20)

        # Frame para organizar os widgets
        frame = ttk.Frame(self)
        frame.pack(fill='both', expand=True, padx=20, pady=10)

        # Dropdown para seleção do carro
        ttk.Label(frame, text="Selecione o Carro:").grid(row=0, column=0, sticky='w', pady=5)
        self.carro_var = tk.StringVar()
        self.carro_dropdown = ttk.Combobox(frame, textvariable=self.carro_var, width=30)
        self.carro_dropdown['values'] = list(self.carros_compactos.keys())
        self.carro_dropdown.grid(row=0, column=1, pady=5)
        self.carro_dropdown.bind("<<ComboboxSelected>>", self.atualizar_info_carro)

        # Dropdown para tipo de combustível
        ttk.Label(frame, text="Tipo de Combustível:").grid(row=1, column=0, sticky='w', pady=5)
        self.combustivel_var = tk.StringVar()
        self.combustivel_dropdown = ttk.Combobox(frame, textvariable=self.combustivel_var, width=30)
        self.combustivel_dropdown['values'] = ["Etanol", "Gasolina"]
        self.combustivel_dropdown.grid(row=1, column=1, pady=5)

        # Dropdown para tipo de percurso
        ttk.Label(frame, text="Tipo de Percurso:").grid(row=2, column=0, sticky='w', pady=5)
        self.percurso_var = tk.StringVar()
        self.percurso_dropdown = ttk.Combobox(frame, textvariable=self.percurso_var, width=30)
        self.percurso_dropdown['values'] = ["Cidade", "Estrada"]
        self.percurso_dropdown.grid(row=2, column=1, pady=5)

        # Entrada para distância
        ttk.Label(frame, text="Distância (km):").grid(row=3, column=0, sticky='w', pady=5)
        self.distancia_entry = ttk.Entry(frame, width=30)
        self.distancia_entry.grid(row=3, column=1, pady=5)

        # Botão de cálculo
        self.calcular_button = ttk.Button(frame, text="Calcular", command=self.calcular, width=20)
        self.calcular_button.grid(row=4, column=0, columnspan=2, pady=20)

        # Label para exibir resultado
        self.resultado_label = ttk.Label(frame, text="", font=('Roboto', 14))
        self.resultado_label.grid(row=5, column=0, columnspan=2, pady=10)

        # Label para exibir informações do carro
        self.info_carro_label = ttk.Label(frame, text="", font=('Roboto', 12))
        self.info_carro_label.grid(row=6, column=0, columnspan=2, pady=10)

    def atualizar_info_carro(self, event):
        carro = self.carro_var.get()
        if carro in self.carros_compactos:
            info = self.carros_compactos[carro]
            self.info_carro_label.config(text=(
                f"Eficiência Energética: {info['Eficiência']} MJ/km\n"
                f"Preço Inicial: R$ {info['Preço']:,.2f}"
            ))
        else:
            self.info_carro_label.config(text="")

    def calcular(self):
        try:
            carro = self.carro_var.get()
            combustivel = self.combustivel_var.get()
            percurso = self.percurso_var.get()
            distancia = float(self.distancia_entry.get())

            if not all([carro, combustivel, percurso]):
                raise ValueError("Por favor, preencha todas as informações")

            info_carro = self.carros_compactos[carro]
            chave_consumo = f"{percurso} ({combustivel.lower()})"
            consumo = info_carro[chave_consumo]

            combustivel_gasto = calcular_consumo(distancia, consumo)
            
            resultado = (f"Para {carro} usando {combustivel} em percurso de {percurso.lower()}:\n"
                         f"Consumo médio: {consumo:.1f} km/l\n"
                         f"Combustível gasto: {combustivel_gasto:.2f} litros\n"
                         f"Distância: {distancia:.1f} km")

            self.resultado_label.config(text=resultado)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
        except KeyError:
            messagebox.showerror("Erro", "Combinação de carro, combustível e percurso inválida")

if __name__ == "__main__":
    app = AplicativoConsumo()
    app.mainloop()
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



