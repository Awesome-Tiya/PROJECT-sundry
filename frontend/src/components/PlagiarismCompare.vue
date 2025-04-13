<template>
    <navbar></navbar> 
    <div class="labels"> 
        <p class="label1">text1</p> 
        <p class="label2">text2</p> 
    </div> 
    <div class="texts"> 
        <textarea class="text1" placeholder="Enter text1" v-model="text1"></textarea> 
        <textarea class="text2" placeholder="Enter text2" v-model="text2"></textarea> 
        <div v-if="similarity_percentage != null && similarity_partial_percentage != null && similarity_without_minor_components != null" class="organise"> 
            <p>similarity percentage: {{ similarity_percentage }}</p> 
            <p>similarity partial percentage: {{ similarity_partial_percentage }}</p> 
            <p>similarity percentage without minor components: {{ similarity_without_minor_components }}</p> 
        </div>
    </div>
    <button @click="comparing">compare</button> 
</template> 

<script lang="ts" setup> 
import navbar from './navbar.vue'; 
import { useCompare } from '../composables/useCompare'; 
import { ref } from 'vue';

const { compare } = useCompare(); 
const text1=ref<string>(''); 
const text2=ref<string>(''); 
const similarity_percentage=ref<number | null>(null); 
const similarity_partial_percentage=ref<number | null>(null); 
const similarity_without_minor_components=ref<number | null>(null); 

const comparing= async () => { 
    if(text1.value.trim() && text2.value.trim()) { 
        const compared= await compare(text1.value, text2.value); 
        if(!compared.error) { 
            similarity_percentage.value=compared.similarity_percentage; 
            similarity_partial_percentage.value=compared.similarity_partial_percentage; 
            similarity_without_minor_components.value=compared.similarity_without_minor_components; 
        } 
        else { 
            alert(compared.error); 
        }
    } 
    else { 
        alert('Enter texts first'); 
    }
}
</script> 

<style scoped> 
button {
    background-color: #b2f2bb;
    font-family: 'Caveat', cursive;
    padding: 10px 45px;
    border: 2px solid black;
    margin-left: 14.4%;
    margin-top: 27.9%; 
    position: fixed;
    border-radius: 27px 9px 20px 9px / 27px 18px 40px 27px;
    cursor: pointer;
    font-size: 24px;
} 
button:hover, .filter-file-upload:hover {
  transform: scale(1.05);
  transition: 0.3s ease;
} 
textarea {
    font-family: 'Caveat', cursive;
    height: 261px;
    width: 189px;
    border: 2px solid black;
    resize: none;
    border-radius: 27px 9px 20px 9px/27px 18px 40px 27px;
    padding: 27px; 
    font-size: 27px;
} 
.texts {
    display: flex;
    margin-top: 0.45%; 
    margin-left: 0%; 
    position: fixed;
    justify-content: center;
    gap: 40px;
} 
.labels {
    display: flex;
    margin-top: 0.45%; 
    margin-left: -70.2%; 
    justify-content: center;
    gap: 243px;
} 
.label1, p, .label2 { 
    font-family: "Caveat", cursive; 
    font-size: 27px;
}
</style>