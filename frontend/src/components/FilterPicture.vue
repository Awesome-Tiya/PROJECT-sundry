<template>
    <div class="background">
        <navbar></navbar>
        <div class="filter-image-inputs">
            <label class="file-upload">
                <input type="file" class="filter-image" @change="handleFileChange" accept="image/*">
                <p class="filter-file-upload">choose photo</p>
                <p>{{ imgName || "no file chosen" }}</p>
                <p class="placeholder"> enter the photo!</p>
            </label>
            <div class="accessories">
                <select name="filter" class="filter-name" v-model="col">
                    <option disabled value="">select filter</option>
                    <option value="blue">blue</option>
                    <option value="green">green</option>
                    <option value="purple">purple</option>
                    <option value="gray">gray</option>
                </select>
                <input type="text" placeholder="name of your new photo" v-model="name">
            </div>
        </div>
        <button @click="generate">generate</button>
    </div>
</template>

<script setup lang=ts>
import navbar from './navbar.vue';
import { ref } from 'vue';
import { useFilter } from '../composables/useFilter';

const { applyColorEffect } = useFilter();
const imgName=ref<string>('');
const col=ref<string>('');
const name=ref<string>('');
const img1=ref<File | null>(null);

//https://img.freepik.com/free-photo/blue-watercolor-texture-with-copyspace-right_24972-147.jpg
//https://img.freepik.com/premium-photo/abstract-water-colour-painted_51764-861.jpg
//https://img.freepik.com/free-vector/hand-painted-abstract-blue-wallpaper-watercolor_23-2149106506.jpg
//https://img.freepik.com/free-vector/doodle-candy-journal-sticker-with-white-border-beige-background-vector_53876-173406.jpg?t=st=1743923214~exp=1743926814~hmac=d761109ebabc2044ebb09a18642b48dd7e3933d873d9414959bf424840574b52&w=900

const handleFileChange=(event: Event) => {
    const img=event.target as HTMLInputElement;
    if(img.files && img.files[0]) {
        img1.value=img.files[0];
        imgName.value=img.files[0].name;
    } else {
        img1.value=null;
        imgName.value='';
    }
}

const generate=() => {
    if(!img1.value) {
        alert("upload an image");
        return;
    }
    if(!col.value) {
        alert("select a filter");
        return;
    }
    if(!name.value) {
        name.value="img1";
    }

    applyColorEffect(col.value, name.value, img1.value); 
    setTimeout(() => { window.open(`http://127.0.0.1:5000/static/${name.value}.jpg`, "_blank"); }, 2000); 
}
</script>

<style scoped>
button {
    background-color: #b2f2bb;
    font-family: 'Caveat', cursive;
    padding: 10px 45px;
    border: 2px solid black;
    margin-left: 42.3%;
    margin-top: 7.2%;
    border-radius: 27px 9px 20px 9px / 27px 18px 40px 27px;
    cursor: pointer;
    font-size: 24px;
}
.background {
    min-height: 100vh;
    background-image: url('/src/assets/doodle-candy-journal-sticker-with-white-border-beige-background-vector_53876-173406-removebg-preview.png');
    background-repeat: repeat;
    background-size: 200px 200px; /* size of the candy */
    background-position: center;
}
.filter-image-inputs {
    display: flex;
    margin-top: 7.2%;
    justify-content: center;
    gap: 40px;
}
.filter-file-upload {
    border: 2px solid black;
    margin-left: 27%;
    border-radius: 27px 9px 20px 9px / 27px 18px 40px 27px;
    background-color: #fff0f6;
    width: 126px;
    font-size: 27px;
}
button:hover, .filter-file-upload:hover {
  transform: scale(1.05);
  transition: 0.3s ease;
}
.file-upload {
    border: 2px solid black;
    padding: 10px;
    align-content: center;
    text-align: center;
    border-radius: 27px 9px 20px 9px / 27px 18px 40px 27px;
    margin-left: -9%;
    font-size: 18px;
    width: 279px;
    height: 180px;
    font-family: 'Caveat', cursive;
    cursor: pointer;
    overflow: hidden;
    position: relative;
}
.file-upload input[type="file"] {
  display: none;
}
.placeholder {
  color: #777;
  background-color: rgb(240, 241, 255);
  margin-left: 33.3%;
  border-radius: 10px;
  width: 99px;
  font-size: 16px;
}
.filter-name {
    border: 2px solid black;
    border-radius: 27px 9px 20px 9px / 27px 18px 40px 27px;
    background-color: #fff0f6;
    text-align: center;
    padding: 9px;
    cursor: pointer;
    font-family: 'Caveat', cursive;
    width: 180px;
    font-size: 20.7px;
}
.accessories {
  display: flex;
  flex-direction: column; /* Stack dropdown and input vertically */
  margin-left: 9%;
  gap: 20px;
  justify-content: center;
}
.accessories input[type="text"] {
  border: none;
  border-bottom: 2px solid black;
  padding: 9px;
  background-color: #ffffff;
  outline: none;
  font-family: 'Caveat', cursive;
  width: 180px;
  font-size: 20px;
}

</style>
