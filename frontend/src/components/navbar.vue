<template>
    <div class="navbar">
        <router-link to="/"> home </router-link>
    </div> 
</template>

<script setup>

</script>

<style scoped>
.navbar {
    background-color: #a5d8ff;
    border: 2px solid black;
    padding: 4px 40px;
    border-radius: 27px 9px 20px 9px/27px 18px 40px 27px;
    font-family: 'Caveat', cursive;
    height: auto;
    font-size: 1.8rem;

}
a {
  text-decoration: none;
  position: relative;
  display: inline-block;
  padding: 4px 8px;
  color: black;
  transition: transform 0.2s ease-in-out;
}

a:hover {
  transform: scale(1.05);
}

</style>

