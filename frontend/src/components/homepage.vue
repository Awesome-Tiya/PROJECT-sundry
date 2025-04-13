<template>
  <div class="template">
    <div class="project-title">
      <span class="sparkle"></span>
      <p>PROJECT-sundry</p>
      <span class="sparkle"></span>
    </div>
    <div class="tab-group">
      <router-link class="color-filter" to="/color-effect">
        <div class="box-content">
        <img src="/src/assets/sunrise-mountain-sticker-design-element-vector_53876-167971-removebg-preview.png" alt="Color Filter Icon" />
        <span>filter on your photo!</span>
      </div>
      </router-link>
      <router-link class="book" to="/books">
        <div class="box-content">
          <img src="/src/assets/book-read-book-day-icon_24640-133870-removebg-preview.png" alt="Color Filter Icon" />
          <span> book suggestion! </span>
        </div>
      </router-link>
    </div>
    <div class="tab-group">
      <router-link class="qrgen" to="/genqr">
        <div class="box-content">
          <img src="/src/assets/qr-code-box_78370-5864-removebg-preview.png" alt="Color Filter Icon" />
          <span> qr code generator! </span>
        </div>
      </router-link>
      <router-link class="text" to="/compare">
        <div class="box-content">
          <img src="/src/assets/education-concept-with-supplies_23-2149935204-removebg-preview.png" alt="Color Filter Icon" />
          <span> compare texts for plagiarism! </span>
        </div>
    </router-link>
    </div>
  </div>
</template>

<script setup lang="ts">

</script>

<style scoped>
.sparkle {
  width: 14px;
  height: 14px;
  border: 2px solid black;
  border-radius: 2px 9px 20px 9px / 2px 18px 40px 27px;;
  background-color: #e7f5ff;
  transform: rotate(45deg);
}
p {
  font-family: 'Caveat', cursive;
  font-size: 27.9px;
  text-align: center;
}
.project-title {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 15px; /* spacing between sparkles and title */
  margin-top: 2.7px;
}
.template {
  background-color: #e3fafc;
  background-size: cover;
  min-height: 100vh;
}
.tab-group {
  display: flex;
  margin-top: 2.7%;
  justify-content: center;
  gap: 90px;
}
.color-filter, .book, .qrgen, .text {
  justify-content: center;
  height: 180px;
  width: 270px;
  border: 2px solid black;
  display: flex;
  border-radius: 27px 9px 20px 9px / 27px 18px 40px 27px;
  text-align: center;
  align-items: flex-end;
  padding: 10px;
}
.color-filter:hover, .book:hover, .qrgen:hover, .text:hover {
  transform: scale(1.03);
  transition: 0.3s ease;
}
.color-filter {
  background-color: #99e9f2;
  margin-left: 3.6%;
}
.book {
  background-color: #b2f2bb;
}
.qrgen {
  background-color: #ffec99;
}
.text {
  background-color: #fcc2d7;
  margin-right: 9%;
}
.box-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between; /* space between image and text */
  height: 100%;
  width: 100%;
}

.box-content img {
  width: 180px;
  height: 180px;
  margin-top: -20.7px;
}

.box-content span {
  padding-bottom: 10px;
}
a {
  text-decoration: none;
  font-family: 'Caveat', cursive;
  color: black;
  cursor: pointer;
  font-size: 20.7px;
}
</style>
