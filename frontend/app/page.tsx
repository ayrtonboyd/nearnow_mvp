"use client";

import { useState } from "react";

export default function Home() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

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

  const exampleQueries = [
    "cosy café open for lunch",
    "dog-friendly pub for a quiet pint",
    "trendy café with WiFi",
    "pub with outdoor seating",
    "vegetarian-friendly lunch spot"
  ];
  

  return (
    <main className="flex flex-col items-center min-h-screen p-6 bg-[#f6f4ee]">
      <img 
        src="/logo.png"
        alt="NearNow logo"
        className="w-50 mb-4"
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
          className="w-full border border-gray-300 rounded-lg p-3 mb-4 text-black focus:outline-none focus:ring-2 focus:ring-[#449787]"
        />

        <button
          onClick={handleSearch}
          disabled={loading}
          className="w-full bg-[#449787] text-white py-3 rounded-lg font-medium hover:bg-[#538d90] transition disabled:bg-[#538d90]"
        >
          {loading ? (
            <span className="animate-pulse">Searching…</span>
          ) : (
            "Search"
          )}
        </button>

        

        {/* Example Searches */}
        <div className="mt-4">
          <p className="text-sm text-black mb-2">Try one of these:</p>

          <div className="flex flex-wrap gap-2">
            {exampleQueries.map((item, index) => (
              <button
                key={index}
                onClick={() => {
                  setQuery(item);
                  handleSearch();
                }}
                className="px-3 py-1 bg-[#449787] hover:bg-[#538d90] text-sm rounded-full transition"
              >
                {item}
              </button>
            ))}
          </div>
        </div>


        {error && (
          <p className="mt-3 text-red-600 text-sm font-medium">{error}</p>
        )}
      </div>

      {/* Response Box */}
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
