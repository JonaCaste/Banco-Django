<template>

  <div class="app" id="app">
    <div class="header">
      <h1>Banco-Django</h1>
    </div>
  </div>

  <!-- <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </div>
  <router-view/> -->
</template>

<script>
  export default {
    name:'App',

    data : function(){

    },

    methods: {

    },

    created: function(){

    }
  }
</script>

<style>
  .header{
    margin: 0;
    padding: 0;
    width: 100%;
    height: 10vh;
    min-height: 100px;
    background-color: #283747;
    color: #e5e7e9;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .header h1{
    width: 20%;
    text-align: center;
  }
</style>
