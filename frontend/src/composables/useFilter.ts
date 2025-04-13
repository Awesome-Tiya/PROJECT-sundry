import axios from 'axios';

const baseUrl = import.meta.env.DEV
  ? "http://127.0.0.1:5000/color-effect" // local dev
  : "https://crispy-couscous-5p5wrgj9x7j2v4x9-5000.app.github.dev/color-effect"; // hosted


export function useFilter() {
    const applyColorEffect= async(col: string, name: string, img1: File) => {
        try { 
            const formData = new FormData();
            formData.append('col', col);
            formData.append('name', name);
            formData.append('img1', img1);

            const response = await axios.post(baseUrl, formData, {
                headers: {
                  'Content-Type': 'multipart/form-data',
                },
              });
            return response.data;
        } catch(error) {
            console.error("Error generating image", error);
            return { error: error.response?.data?.message || "failed to generate image" };
        }
    };
    return { applyColorEffect }
}
