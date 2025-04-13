<template>
    <navbar></navbar>
    <textarea placeholder="enter the data or link to convert it to a qr code!" v-model="qrText" class="qr-text"></textarea>
    <div class="color-options">
        <p class="fill-color">fill color</p>
        <input type="color" class="color1" v-model="fillColor">
        <input type="color" class="color2" v-model="backColor">
        <p class="back-color">back color</p>
    </div>
    <button @click="generate">generate</button> 
</template>

<script setup lang=ts>
import navbar from './navbar.vue';
import { ref } from 'vue';
import { useGenqr } from '../composables/useGenqr';

const { genqr, imgUrl } = useGenqr();

const qrText=ref<string>("");
const fillColor=ref<string>("#1e1e1e");
const backColor=ref<string>("#ffffff");

const generate= async () => {
  console.log("generate clicked");
  if(qrText.value.trim()) {
    const response= await genqr(qrText.value, fillColor.value, backColor.value);
    console.log("qr response", response); 
    window.open("http://localhost:5000/static/siteqr.png", "_blank"); 
  }
  else {
    alert('Enter some text');
  }
}

</script>

<style scoped>
.qr-text {
    font-family: 'Caveat', cursive;
    height: 189px;
    width: 261px;
    border: 2px solid black;
    resize: none;
    border-radius: 27px 9px 20px 9px/27px 18px 40px 27px;
    padding: 27px;
    margin-top: 4%;
    margin-left: 36%;
    font-size: 27px;
}
button {
    background-color: #b2f2bb;
    font-family: 'Caveat', cursive;
    padding: 10px 45px;
    border: 2px solid black;
    margin-left: 42.3%;
    margin-top: 2%;
    border-radius: 27px 9px 20px 9px / 27px 18px 40px 27px;
    cursor: pointer;
    font-size: 24px;
} 
button:hover, .filter-file-upload:hover {
  transform: scale(1.05);
  transition: 0.3s ease;
} 
.fill-color {
    background-color: #fff0f6;
    font-family: 'Caveat', cursive;
    padding: 10px 18px;
    border: 2px solid black;
    border-radius: 27px 9px 20px 9px / 27px 18px 40px 27px;
    font-size: 24px;
    white-space: nowrap;
}
.color1,
.color2 {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  border: 2px solid black;
  cursor: pointer;
  padding: 0;
  background: none;
}

/* Style the inside circle (color swatch) */
.color1::-webkit-color-swatch,
.color2::-webkit-color-swatch {
  border: none;
  border-radius: 50%;
  padding: 0;
}

.color1::-moz-color-swatch,
.color2::-moz-color-swatch {
  border: none;
  border-radius: 50%;
}

.back-color {
    background-color: #fff0f6;
    font-family: 'Caveat', cursive;
    padding: 10px 18px;
    border: 2px solid black;
    border-radius: 27px 9px 20px 9px / 27px 18px 40px 27px;
    font-size: 24px;
    white-space: nowrap;
}
.color-options {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 54px;
}
</style>   
