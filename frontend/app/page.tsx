"use client";

import { useState, useEffect } from "react";

export default function Home() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // Pool of rotating example questions
  const allExampleQueries = [
    "Cosy café open for lunch",
    "Dog-friendly pub for a quiet pint",
    "Trendy café with WiFi",
    "Pub with outdoor seating",
    "Vegetarian-friendly lunch spot",
    "Quiet café for remote work",
    "Late-night dessert café",
    "Family-friendly brunch spot",
    "High-end pub for a nice dinner",
    "Budget-friendly café under £7",
    "Scenic café with outdoor seating",
    "Cosy pub with real ales",
    "Instagrammable café",
    "Vegan-friendly café",
    "Gluten-free lunch spot",
    "Café open early for breakfast",
    "Pub open late on weekends",
    "Heritage café with character",
    "Stylish modern coffee shop",
    "Relaxed pub for catching up"
  ];

  const [suggested, setSuggested] = useState<string[]>([]);

  useEffect(() => {
    // Pick 3 random suggestions each refresh
    const shuffled = [...allExampleQueries].sort(() => 0.5 - Math.random());
    setSuggested(shuffled.slice(0, 3));
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
    <main className="flex flex-col items-center min-h-screen p-6 bg-[#f6f4ee]">
      
      {/* Logo */}
      <img 
        src="/logo.png"
        alt="NearNow logo"
        className="w-48 mb-6"
      />

      {/* Search Card */}
      <div className="w-full max-w-xl bg-white shadow-lg rounded-xl p-6 border border-gray-200">
        <label className="block mb-2 font-medium text-black">
          What are you looking for?
        </label>

        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="e.g., cosy café open for lunch"
          className="w-full border border-gray-300 rounded-lg p-3 mb-4 
                     text-black focus:outline-none focus:ring-2 focus:ring-[#449787]"
        />

        <button
          onClick={handleSearch}
          disabled={loading}
          className="w-full bg-[#449787] text-white py-3 rounded-lg font-medium 
                     hover:bg-[#538d90] transition disabled:bg-[#538d90]"
        >
          {loading ? (
            <span className="animate-pulse">Searching…</span>
          ) : (
            "Search"
          )}
        </button>

        {/* NEW — Rotating 3-Box Suggestions */}
        <div className="mt-6">
          <p className="text-sm text-black mb-3">Try one of these:</p>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
            {suggested.map((item, index) => (
              <div
                key={index}
                onClick={() => setQuery(item)}
                className="cursor-pointer bg-white border border-gray-300 
                           hover:border-[#449787] hover:shadow-md 
                           p-3 rounded-lg text-sm 
                           transition leading-snug text-black"
              >
                {item}
              </div>
            ))}
          </div>
        </div>

        {error && (
          <p className="mt-3 text-red-600 text-sm font-medium">{error}</p>
        )}
      </div>

      {/* Response Box */}
      {response && (
        <div className="w-full max-w-xl mt-6 bg-white shadow-md p-6 rounded-xl 
                        border border-gray-200 whitespace-pre-line">
          <h2 className="text-xl font-semibold mb-2 text-[#449787]">
            Results
          </h2>
          <p className="text-gray-800 leading-relaxed">{response}</p>
        </div>
      )}
    </main>
  );
}
