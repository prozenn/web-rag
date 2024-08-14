'use client';

import {useState} from "react";
import {Markdown} from "react-showdown";

export default function Home() {
    const [question, setQuestion] = useState("");
    const [response, setResponse] = useState("");

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setResponse("");

        try {
            const res = await fetch("http://localhost:8000/chat/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({question}),
            });

            if (!res.body) {
                throw new Error("ReadableStream not supported");
            }

            const reader = res.body.getReader();
            const decoder = new TextDecoder();
            let result = "";

            while (true) {
                const {done, value} = await reader.read();
                if (done) break;
                result += decoder.decode(value, {stream: true});
                setResponse((prev) => prev + decoder.decode(value, {stream: true}));
            }
        } catch (error) {
            console.error("Error fetching response:", error);
        }
    };

    return (
        <main className="flex w-full min-h-screen flex-col items-center p-24 gap-10">
            <form onSubmit={handleSubmit} className="w-full">
                <div className="flex items-center justify-between gap-4">
                    <input
                        id="question"
                        type="text"
                        value={question}
                        onChange={(e) => setQuestion(e.target.value)}
                        className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    />
                    <button
                        type="submit"
                        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                    >
                        Submit
                    </button>
                </div>
            </form>
            <div
                className="w-full bg-white shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight">
                <Markdown markdown={response}/>
            </div>
        </main>
    );
}