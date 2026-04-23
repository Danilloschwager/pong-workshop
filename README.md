# 🏓 Pong Workshop

> Uma implementação moderna do clássico Pong, projetada como base educacional para ensino de fundamentos de desenvolvimento de jogos e arquitetura frontend.

---

## 📖 Visão Geral

Este projeto tem como objetivo ensinar, de forma prática e progressiva, os princípios fundamentais por trás de jogos 2D em tempo real, utilizando tecnologias web nativas.

A proposta vai além de simplesmente recriar o Pong — o foco está em **entender os mecanismos internos de um game loop**, **organização de código**, e **separação de responsabilidades**.

---

## 🧠 Conceitos Abordados

- Game Loop (Update / Render cycle)
- Detecção de colisão (AABB simplificado)
- Manipulação de input (event-driven)
- Física básica (velocidade, direção e reflexão)
- Controle de estado (game state management)
- Renderização com Canvas API
- Estruturação de código modular

---

## 🏗️ Arquitetura

O projeto segue uma abordagem simples, porém escalável, baseada em separação lógica entre:

- **Rendering Layer** → Responsável por desenhar os elementos na tela  
- **Game Logic Layer** → Responsável pelas regras do jogo  
- **Input Layer** → Captura e trata eventos do usuário  
- **State Management** → Mantém o estado atual do jogo  

Essa divisão facilita manutenção, testes e evolução do projeto.

---

## ⚙️ Tecnologias e Ferramentas

### 🧩 Core

- **HTML5**
  - Estrutura base da aplicação
  - Container do canvas

- **CSS3**
  - Estilização e layout
  - Responsividade básica

- **JavaScript (Vanilla)**
  - Linguagem principal do projeto
  - Sem frameworks, focando em fundamentos

---

### 🎨 Renderização

- **Canvas API**
  - Renderização 2D em tempo real
  - Controle total sobre pixels e animações
  - Ideal para jogos simples e aprendizado de gráficos

---

### ⏱️ Execução e Loop

- **requestAnimationFrame**
  - Controle eficiente do loop de renderização
  - Sincronização com o refresh rate do navegador
  - Melhor performance comparado a `setInterval`

---

### 🎮 Input Handling

- **Event Listeners (Keyboard / Mouse)**
  - Captura de inputs do usuário
  - Arquitetura orientada a eventos

---

### 🧪 Ambiente de Desenvolvimento

- Navegador moderno (Chrome, Edge, Firefox)
- DevTools para debug e profiling
- Git para versionamento

---

## 🚀 Como Executar

```bash
# Clone o repositório
git clone https://github.com/FilipeHSAraujo/pong-workshop.git

# Acesse o diretório
cd pong-workshop
