"use client";

import { useState, useEffect } from "react";
import { FiSend } from "react-icons/fi"; // paper-plane icon

export default function Home() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [suggestions, setSuggestions] = useState<string[]>([]);

  // Full suggestion pool (20 rotating)
  const suggestionPool = [
    "Cosy café open for lunch",
    "Dog-friendly pub for a quiet pint",
    "Trendy café with WiFi",
    "Pub with outdoor seating",
    "Vegetarian-friendly lunch spot",
    "Late-night coffee place",
    "Quiet café to work from",
    "Scenic pub for Sunday lunch",
    "Budget-friendly café",
    "Premium restaurant for dinner",
    "Instagrammable brunch spot",
    "Heritage café in town",
    "Family-friendly pub",
    "Vegan-friendly breakfast",
    "Gluten-free café options",
    "Cosy café open early",
    "Pub with a lively atmosphere",
    "Café with outdoor tables",
    "Dog-friendly brunch place",
    "Quiet spot for reading"
  ];

  // Pick 3 random suggestions on each page load
  useEffect(() => {
    const shuffled = [...suggestionPool].sort(() => 0.5 - Math.random());
    setSuggestions(shuffled.slice(0, 3));
  }, []);

  const handleSearch = async () => {
    setError("");
    setResponse("");

    if (!query.trim()) {
      setError("Please enter a search.");
      return;
    }

    setLoading(true);

    try {
      const res = await fetch(
        "http://localhost:8000/api/recommend?query=" +
          encodeURIComponent(query)
      );

      if (!res.ok) {
        throw new Error("Backend error");
      }

      const data = await res.json();

      setResponse(
        data.answer ||
          data.response ||
          data.content ||
          "No response received."
      );
    } catch (err) {
      setError("Unable to connect to the NearNow server.");
    }

    setLoading(false);
  };

  return (
    <main className="flex flex-col items-center min-h-screen p-6 bg-[#f6f4ee] text-black">

      {/* Logo */}
      <img
        src="/logo.png"
        alt="NearNow logo"
        className="w-45 mb-4 mt-4"
      />

      {/* Tagline + intro */}
      <h1 className="text-2xl font-bold text-center mb-2">
        Be a local, anywhere.
      </h1>

      <p className="text-center max-w-xl text-gray-700 mb-8">
        NearNow is your friendly Kendal-based AI concierge.
        Ask naturally and I’ll recommend the best cafés and pubs based on
        what you’re in the mood for. This demo currently works with Kendal venues only.
      </p>

      {/* Main Container */}
      <div className="w-full max-w-xl bg-white shadow-lg rounded-2xl p-6 border border-gray-200">

        {/* Greeting */}
        <h2 className="text-lg text-center font-medium mb-4">
          How can I help you today?
        </h2>

        {/* Input Field with embedded button */}
        <div className="flex items-center border border-gray-300 rounded-xl px-3 mb-4 bg-white focus-within:ring-2 focus-within:ring-[#449787]">
          <input
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Ask NearNow..."
            className="w-full p-3 text-black focus:outline-none"
          />

          <button
            onClick={handleSearch}
            disabled={loading}
            className="p-2 text-[#449787] hover:text-[#2f6e65] transition disabled:text-gray-400"
          >
            <FiSend size={22} />
          </button>
        </div>

        {/* Suggested Questions */}
        <h3 className="text-center font-medium mb-3">Suggested Questions:</h3>

        {/* Cards Row */}
        <div className="flex gap-3 overflow-x-auto pb-2">
          {suggestions.map((item, index) => (
            <button
              key={index}
              onClick={() => setQuery(item)} // does NOT auto-search
              className="min-w-[150px] max-w-[150px] bg-white border border-[#449787] rounded-xl p-3 
                         text-sm text-left hover:bg-[#e7f4f2] hover:border-[#2f6e65] transition"
            >
              {item}
            </button>
          ))}
        </div>

        {error && (
          <p className="mt-3 text-red-600 text-sm font-medium">{error}</p>
        )}
      </div>

      {/* Results */}
      {response && (
        <div className="w-full max-w-xl mt-6 bg-white shadow-md p-6 rounded-xl border border-gray-200 whitespace-pre-line">
          <h2 className="text-xl font-semibold mb-2 text-[#449787]">
            Results
          </h2>
          <p className="text-gray-800 leading-relaxed">{response}</p>
        </div>
      )}
    </main>
  );
}
