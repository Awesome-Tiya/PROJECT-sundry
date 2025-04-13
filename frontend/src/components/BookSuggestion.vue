<template>
    <navbar></navbar> 
    <div class="page"> 
        <div class="book-suggest">
            <input type="text" placeholder="enter genre" v-model="genre"> 
            <button @click="suggest">suggest</button> 
        </div> 
        <div class="loading" v-if="loading">Loading</div> 
        <div v-else> 
            <div class="suggestions" v-if="booksarray != null && Array.isArray(booksarray)"> 
                <div v-for="(book, index) in booksarray" :key="index" class="book-item"> 
                    {{ typeof book === 'string' ? book: book.title }}
                </div> 
            </div> 
        </div>
    </div> 
</template> 

<script lang="ts" setup> 
import navbar from './navbar.vue'; 
import { useBooks } from '../composables/useBooks'; 
import { ref } from 'vue';

const { books } = useBooks(); 
const booksarray = ref<object | null>(null); 
const genre=ref<string>(''); 
const loading=ref<boolean>(false); 

const suggest= async () => { 
    loading.value=true; 
    if(genre.value) { 
        const booksuggestions= await books(genre.value); 
        if(!booksuggestions.error) { 
            if(booksuggestions.genre) { 
                loading.value=false; 
                alert(booksuggestions.genre); 
            } else { 
                loading.value=false; 
                booksarray.value=booksuggestions.books; 
            } 
        } 
        else { 
            loading.value=false; 
            alert(booksuggestions.error); 
        } 
    } else { 
        loading.value=false; 
        alert('Enter genre'); 
    }
}
</script> 

<style scoped> 
button {
    background-color: #b2f2bb;
    font-family: 'Caveat', cursive;
    padding: 10px 45px;
    border: 2px solid black; 
    margin-top: 9%;
    border-radius: 27px 9px 20px 9px / 27px 18px 40px 27px;
    cursor: pointer;
    font-size: 24px;
} 
button:hover, .filter-file-upload:hover {
  transform: scale(1.05);
  transition: 0.3s ease;
} 
.page {
    display: flex; 
    justify-content: space-between;
    gap: 100px;
} 
.book-suggest {
  display: flex; 
  margin-top: 9%; 
  margin-left: 9%;
  flex-direction: column;
  gap: 20px;
} 
input[type="text"] {
  border: none;
  border-bottom: 2px solid black;
  padding: 9px;
  background-color: #ffffff;
  outline: none;
  font-family: 'Caveat', cursive;
  width: 180px;
  font-size: 20px;
} 
.book-item { 
    border: 2px solid #e3fafc; 
    padding: 9px; 
    border-radius: 27px 9px 20px 9px / 27px 18px 40px 27px; 
    word-break: break-word;
    background-color: #e3fafc; 
    box-shadow: 2px 2px 1px rgba(153, 233, 242, 1);
} 
.loading {
  font-size: 24px; 
  color: #888; 
  font-family: 'Caveat', cursive; 
  margin-right: 36%; 
  margin-top: 9%;
  align-content: center; 
  padding: 20px;
} 
.suggestions { 
  display: grid; 
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); 
  gap: 9px; 
  padding: 36px;
  margin-top: 18px; 
  font-size: 22px; 
  width: 90%; 
  font-family: 'Caveat', cursive; 
  flex-wrap: wrap; 
}
</style> 