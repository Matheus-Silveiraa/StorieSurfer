# Instagram Stories Automation Bot

Bot de automação desenvolvido em Python que simula interações humanas no Instagram através de controle de interface gráfica (GUI). O projeto demonstra habilidades avançadas em **automação de processos**, **manipulação de teclado/mouse** e **lógica de navegação multiplataforma**.

## Objetivo
Automatizar a visualização de stories no Instagram para estudo de algoritmos de engajamento, demonstrando capacidade de criar soluções que interagem diretamente com interfaces gráficas de usuário.

## Funcionalidades Técnicas
- **Navegação Inteligente:** Abre automaticamente o Instagram via navegador ou aplicativo nativo
- **Controle de GUI:** Utiliza `pyautogui` e `pynput` para simular pressionamento de teclas e cliques
- **Multiplataforma:** Lógica adaptativa para Windows 10 e Windows 11
- **Sistema de Pausas:** Timing controlado para simular comportamento humano
- **Interface Interativa:** Menu de configuração via terminal para selecionar ambiente de execução

## Stack Tecnológica
- **Python 3** - Linguagem principal
- **PyAutoGUI** - Automação de controle de mouse e teclado
- **Pynput** - Controle e monitoramento de dispositivos de entrada
- **Time** - Controle de timing e delays naturais

## Arquitetura do Bot
```python
# Fluxo principal:
1. Configuração inicial (SO, ambiente de execução)
2. Abertura automática do Instagram
3. Navegação até a seção de stories
4. Loop controlado de visualização
5. Timing personalizado entre ações
