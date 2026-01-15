import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import LandingPage from "./components/Home";
import Chatbot from "./components/ChatBotApp.jsx"; // <-- your existing chatbot component

const API_URL = "https://ai-solution-customer-service-1.onrender.com/api/chat";
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/chatbot" element={<Chatbot />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
