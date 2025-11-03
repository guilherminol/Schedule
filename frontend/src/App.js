import React, { useState, useRef, useEffect } from 'react';
import './App.css';

function App() {
  const [currentMessage, setCurrentMessage] = useState('');
  const [chatHistory, setChatHistory] = useState([]);
  const chatContainerRef = useRef(null);

  // Efeito para rolar para a última mensagem
  useEffect(() => {
    if (chatContainerRef.current) {
      chatContainerRef.current.scrollTop = chatContainerRef.current.scrollHeight;
    }
  }, [chatHistory]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!currentMessage.trim()) return;

    // Adiciona a mensagem do usuário ao histórico
    const userMessage = { sender: 'user', text: currentMessage };
    setChatHistory(prev => [...prev, userMessage]);
    setCurrentMessage('');

    try {
      // Envia a mensagem para a API
      const response = await fetch('http://127.0.0.1:8000/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: currentMessage }),
      });

      const data = await response.json();

      // Adiciona a resposta do bot ao histórico
      setChatHistory(prev => [...prev, { sender: 'bot', text: data.answer }]);
    } catch (error) {
      console.error('Erro ao enviar mensagem:', error);
      setChatHistory(prev => [...prev, {
        sender: 'bot',
        text: 'Desculpe, ocorreu um erro ao processar sua mensagem. Tente novamente mais tarde.'
      }]);
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-header">
        <h1>SaúdeConecta</h1>
        <p className="subtitle">Assistente Virtual de Saúde</p>
      </div>
      
      <div className="chat-messages" ref={chatContainerRef}>
        {chatHistory.map((message, index) => (
          <div
            key={index}
            className={`message ${message.sender === 'user' ? 'user-message' : 'bot-message'}`}
          >
            {message.text}
          </div>
        ))}
      </div>

      <form onSubmit={handleSubmit} className="chat-input-form">
        <input
          type="text"
          value={currentMessage}
          onChange={(e) => setCurrentMessage(e.target.value)}
          placeholder="Digite sua pergunta aqui..."
          className="chat-input"
        />
        <button type="submit" className="send-button">
          Enviar
        </button>
      </form>
    </div>
  );
}

export default App;