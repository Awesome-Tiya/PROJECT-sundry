import axios from 'axios';
import { ref } from 'vue';

const baseUrl = import.meta.env.DEV
  ? "http://127.0.0.1:5000/genqr" // local dev
  : "https://crispy-couscous-5p5wrgj9x7j2v4x9-5000.app.github.dev/genqr"; // hosted

const imgUrl=ref<string>("");

export function useGenqr() {
    const genqr= async(site: string, color1: string, color2: string) => {
        try {
            const response= await axios.post(baseUrl, {
                site, color1, color2
            });
            imgUrl.value= baseUrl + response.data.image_url;
            return response.data;
        } catch(error) {
            console.error("Error generating qr code", error);
            return { error: error.response?.data?.message || "failed to generate qr code" };
        }
    };
    return { genqr, imgUrl }
}
