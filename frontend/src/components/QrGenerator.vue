<template>
  <navbar></navbar>

  <div class="qr-container">
    <textarea
        placeholder="enter the data or link to convert it to a qr code!"
        v-model="qrText"
        class="qr-text"
        :disabled="isLoading"
    ></textarea>

    <div class="color-options">
      <p class="fill-color">fill color</p>
      <input type="color" class="color1" v-model="fillColor" :disabled="isLoading">
      <input type="color" class="color2" v-model="backColor" :disabled="isLoading">
      <p class="back-color">back color</p>
    </div>

    <button @click="generateQrCode" :disabled="isLoading || !qrText.trim()" class="generate-button">
      {{ isLoading ? 'Generating...' : 'generate' }}
    </button>

    <div v-if="qrImageUrl" class="qr-result-display">
      <img :src="qrImageUrl" alt="Generated QR Code" class="qr-image-preview">
      <button @click="forceDownloadQrCode" class="download-button" :disabled="isDownloading">
        {{ isDownloading ? 'Downloading...' : 'Download QR Code' }}
      </button>
    </div>

    <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
  </div>
</template>

<script setup lang="ts">
import navbar from './navbar.vue';
import { ref } from 'vue';
import { useGenqr } from '../composables/useGenqr';

const { genqr } = useGenqr();

const qrText = ref<string>("");
const fillColor = ref<string>("#1e1e1e");
const backColor = ref<string>("#ffffff");
const qrImageUrl = ref<string | null>(null);
const isLoading = ref<boolean>(false);
const isDownloading = ref<boolean>(false);
const errorMessage = ref<string>("");

const getBackendBaseUrl = () => {
  return import.meta.env.DEV
      ? "http://127.0.0.1:5000"
      : "https://crispy-couscous-5p5wrgj9x7j2v4x9-5000.app.github.dev";
}

const generateQrCode = async () => {
  qrImageUrl.value = null;
  errorMessage.value = "";
  if (!qrText.value.trim()) {
    errorMessage.value = 'Enter some text';
    return;
  }
  isLoading.value = true;

  try {
    const response = await genqr(qrText.value, fillColor.value, backColor.value);

    if (response && response.image_url) {
      const backendBaseUrl = getBackendBaseUrl();
      const fullImageUrl = `${backendBaseUrl}${response.image_url}?t=${Date.now()}`;
      qrImageUrl.value = fullImageUrl;
      console.log("QR code generated, URL:", qrImageUrl.value);
    } else {
      throw new Error(response.error || 'Backend did not return a valid image URL.');
    }
  } catch (error: any) {
    errorMessage.value = error.message || "Failed to generate QR code.";
    qrImageUrl.value = null;
  } finally {
    isLoading.value = false;
  }
};

const forceDownloadQrCode = async () => {
  if (!qrImageUrl.value) {
    errorMessage.value = "No QR code generated yet.";
    return;
  }
  errorMessage.value = "";
  isDownloading.value = true;

  try {
    const response = await fetch(qrImageUrl.value, { cache: 'no-store' });
    if (!response.ok) {
      throw new Error(`Failed to fetch image: ${response.status} ${response.statusText}`);
    }
    const blob = await response.blob();

    const objectUrl = URL.createObjectURL(blob);

    const link = document.createElement('a');
    link.href = objectUrl;
    link.download = 'qr-code.png';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);

    URL.revokeObjectURL(objectUrl);

  } catch (error: any) {
    console.error("Download failed:", error);
    errorMessage.value = `Could not download image. ${error.message || ''}`;
  } finally {
    isDownloading.value = false;
  }
};
</script>

<style scoped>
.qr-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  max-width: 700px;
  margin: 20px auto;
  box-sizing: border-box;
  width: 100%;
}

.qr-text {
  font-family: 'Caveat', cursive;
  height: 189px;
  width: 90%;
  max-width: 400px;
  border: 2px solid black;
  resize: none;
  border-radius: 27px 9px 20px 9px/27px 18px 40px 27px;
  padding: 20px;
  margin-top: 20px;
  font-size: 24px;
  display: block;
  box-sizing: border-box;
}

.color-options {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 40px;
  margin-top: 30px;
  width: 90%;
  max-width: 500px;
  flex-wrap: wrap;
}

.fill-color,
.back-color {
  background-color: #fff0f6;
  font-family: 'Caveat', cursive;
  padding: 8px 15px;
  border: 2px solid black;
  border-radius: 27px 9px 20px 9px / 27px 18px 40px 27px;
  font-size: 22px;
  white-space: nowrap;
  margin: 5px;
}

.color1,
.color2 {
  -webkit-appearance: none; -moz-appearance: none; appearance: none;
  width: 45px; height: 45px;
  border-radius: 50%;
  border: 2px solid black; cursor: pointer; padding: 0; background: none;
  vertical-align: middle;
  margin: 5px;
}
.color1::-webkit-color-swatch, .color2::-webkit-color-swatch {
  border: none; border-radius: 50%; padding: 0;
}
.color1::-moz-color-swatch, .color2::-moz-color-swatch {
  border: none; border-radius: 50%;
}

.generate-button {
  background-color: #b2f2bb;
  font-family: 'Caveat', cursive;
  padding: 10px 35px;
  border: 2px solid black;
  margin-top: 30px;
  border-radius: 27px 9px 20px 9px / 27px 18px 40px 27px;
  cursor: pointer;
  font-size: 22px;
  display: block;
  width: auto;
  max-width: 90%;
  box-sizing: border-box;
}
.generate-button:hover:not(:disabled) {
  transform: scale(1.05); transition: 0.3s ease;
}
.generate-button:disabled {
  cursor: not-allowed; opacity: 0.6;
}

.qr-result-display {
  margin-top: 40px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  width: 100%;
}

.qr-image-preview {
  max-width: 250px;
  width: 80%;
  height: auto;
  border: 2px solid black;
  background-color: white;
  padding: 5px;
  box-sizing: border-box;
}

.download-button {
  background-color: #a0c4ff;
  font-family: 'Caveat', cursive;
  padding: 8px 25px;
  border: 2px solid black;
  border-radius: 27px 9px 20px 9px / 27px 18px 40px 27px;
  cursor: pointer;
  font-size: 18px;
  transition: transform 0.3s ease;
  width: auto;
  max-width: 90%;
  box-sizing: border-box;
}
.download-button:hover:not(:disabled) {
  transform: scale(1.05);
}
.download-button:disabled {
  cursor: not-allowed; opacity: 0.6; background-color: #ccc;
}

.error-message {
  color: red;
  text-align: center;
  margin-top: 20px;
  font-size: 16px;
  font-weight: bold;
  width: 90%;
  max-width: 400px;
}

@media (max-width: 600px) {
  .qr-container {
    padding: 15px;
  }

  .qr-text {
    font-size: 20px;
    padding: 15px;
    height: 150px;
    width: 95%;
  }

  .color-options {
    gap: 15px;
    width: 95%;
  }

  .fill-color,
  .back-color {
    font-size: 18px;
    padding: 6px 12px;
  }

  .color1,
  .color2 {
    width: 40px;
    height: 40px;
  }

  .generate-button {
    font-size: 20px;
    padding: 8px 25px;
    margin-top: 25px;
  }

  .qr-image-preview {
     max-width: 200px;
     width: 70%;
  }

  .download-button {
    font-size: 16px;
    padding: 7px 20px;
  }

  .error-message {
    font-size: 14px;
  }
}

</style>
