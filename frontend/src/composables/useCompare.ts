import axios from 'axios';

const baseUrl = import.meta.env.DEV
  ? "http://127.0.0.1:5000/compare" // local dev
  : "https://crispy-couscous-5p5wrgj9x7j2v4x9-5000.app.github.dev/compare"; // hosted


export function useCompare() {
    const compare= async(text_1: string, text_2: string) => {
        try {
            const response= await axios.post(baseUrl, {
                text_1, text_2
            });
            return response.data;
        } catch(error) {
            console.error("Error comparing", error);
            return { error: error.response?.data?.message || "failed to compare" };
        }
    };
    return { compare }
}
