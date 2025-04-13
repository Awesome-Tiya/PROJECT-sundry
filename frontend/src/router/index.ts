import { createRouter, createWebHistory } from 'vue-router';
import homepage from '../components/homepage.vue';
import QrGenerator from '../components/QrGenerator.vue';
import FilterPicture from '../components/FilterPicture.vue'; 
import PlagiarismCompare from '../components/PlagiarismCompare.vue'; 
import BookSuggestion from '../components/BookSuggestion.vue';

const routes= [
    { path: '/',
      component: homepage },
    { path: '/genqr',
      component: QrGenerator },
    { path: '/color-effect',
      component: FilterPicture }, 
    { path: '/compare',
        component: PlagiarismCompare }, 
    { path: '/books',
        component: BookSuggestion }]; 

const router= createRouter({ history: createWebHistory(), routes });
export default router;
