import axios from 'axios';

const baseUrl = import.meta.env.DEV
  ? "http://127.0.0.1:5000/books" // local dev
  : "https://crispy-couscous-5p5wrgj9x7j2v4x9-5000.app.github.dev/books"; // hosted


export function useBooks() {
    const books= async(genre: string) => {
        try {
            const response= await axios.post(baseUrl, { genre }); 
            console.log(response.data); 
            return response.data; 
        } catch(error) {
            console.error("Error fetching books", error);
            return { error: error.response?.data?.message || "failed to fetch books" };
        }
    };
    return { books }
}
