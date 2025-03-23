import { useState } from "react";
import axios from "axios";

export default function Chatbot() {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    setLoading(true);
    setResponse(null);
    try {
      const res = await axios.post("http://127.0.0.1:8000/predict", {
        text: input,
      });
      setResponse(res.data);
    } catch (error) {
      setResponse({ error: "Error fetching response" });
    }
    setLoading(false);
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gradient-to-br from-gray-900 to-green-900 p-6">
      <div className="bg-white p-6 rounded-2xl shadow-xl w-full max-w-md text-center">
        <h1 className="text-2xl font-bold text-green-800">NLP Chatbot</h1>
        <form onSubmit={handleSubmit} className="mt-4">
          <input
            type="text"
            placeholder="Ask a question..."
            className="w-full p-3 border rounded-lg focus:ring focus:ring-green-300 text-gray-900"
            value={input}
            onChange={(e) => setInput(e.target.value)}
          />
          <button
            type="submit"
            className="w-full mt-3 p-3 bg-green-700 text-white rounded-lg hover:bg-green-800"
            disabled={loading}
          >
            {loading ? "Thinking..." : "Ask"}
          </button>
        </form>
        {response && (
          <div className="mt-4 p-4 bg-gray-100 rounded-lg text-gray-800">
            {response.error ? (
              <p className="text-red-600">{response.error}</p>
            ) : (
              <>
                <p><strong>Category:</strong> {response.category}</p>
                <p><strong>Sentiment:</strong> {response.sentiment}</p>
                <p><strong>Urgency:</strong> {response.urgency}</p>
              </>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
// import { useState } from "react";
// import axios from "axios";

// export default function Chatbot() {
//   const [input, setInput] = useState("");
//   const [response, setResponse] = useState(null);
//   const [loading, setLoading] = useState(false);

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     if (!input.trim()) return;

//     setLoading(true);
//     setResponse(null);
//     try {
//       const res = await axios.post("http://127.0.0.1:8000/predict", {
//         text: input,
//       });
//       setResponse(res.data);
//     } catch (error) {
//       setResponse({ error: "Error fetching response" });
//     }
//     setLoading(false);
//   };

//   return (
//     <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-6">
//       <div className="bg-white p-6 rounded-2xl shadow-lg w-full max-w-md">
//         <h1 className="text-2xl font-bold text-center text-gray-800 mb-4">NLP Chatbot</h1>
//         <form onSubmit={handleSubmit} className="flex flex-col gap-3">
//           <input
//             type="text"
//             placeholder="Ask a question..."
//             className="w-full p-3 border rounded-lg focus:ring focus:ring-blue-300"
//             value={input}
//             onChange={(e) => setInput(e.target.value)}
//           />
//           <button
//             type="submit"
//             className="w-full p-3 bg-blue-500 text-white rounded-lg hover:bg-blue-600"
//             disabled={loading}
//           >
//             {loading ? "Thinking..." : "Ask"}
//           </button>
//         </form>

//         {loading && (
//           <div className="mt-4 text-center text-gray-600 animate-pulse">Analyzing...</div>
//         )}

//         {response && (
//           <div className="mt-4 p-4 bg-gray-100 rounded-lg text-gray-700 space-y-2">
//             {response.error ? (
//               <p className="text-red-500">{response.error}</p>
//             ) : (
//               <>
//                 <p><strong>Response:</strong> {response.category}</p>
//                 <p><strong>Sentiment:</strong> {response.sentiment || "N/A"}</p>
//                 <p><strong>Urgency:</strong> {response.urgency || "N/A"}</p>
//               </>
//             )}
//           </div>
//         )}
//       </div>
//     </div>
//   );
// }
