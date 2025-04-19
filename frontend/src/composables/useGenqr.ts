import axios, { AxiosError } from 'axios';

const baseUrl = import.meta.env.DEV
    ? "http://127.0.0.1:5000/genqr"
    : "https://crispy-couscous-5p5wrgj9x7j2v4x9-5000.app.github.dev/genqr";

interface QrSuccessResponse {
    image_url: string;
    message?: string;
    error?: never;
}

interface QrErrorResponse {
    error: string;
    image_url?: never;
}

export function useGenqr() {
    const genqr = async (site: string, color1: string, color2: string): Promise<QrSuccessResponse | QrErrorResponse> => {
        try {
            const response = await axios.post<QrSuccessResponse>(baseUrl, {
                site,
                color1,
                color2
            });

            if (response.data && response.data.image_url) {
                return response.data;
            } else {
                return { error: "Backend response is missing the image URL." };
            }

        } catch (error) {
            let errorMessage = "Failed to generate QR code due to an unknown error.";
            if (axios.isAxiosError(error)) {
                const axiosError = error as AxiosError<any>;
                errorMessage = axiosError.response?.data?.message || axiosError.response?.data?.error || axiosError.message;
            } else if (error instanceof Error) {
                errorMessage = error.message;
            }
            return { error: errorMessage };
        }
    };

    return { genqr };
}