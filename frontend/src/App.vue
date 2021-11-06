<template>

  <div class="app" id="app">
    <div class="header">
      <h1>Banco-Django</h1>

      <nav>
        <button v-if="is_auth">Inicio</button>   <!-- solo carga si se cumple el condicional -->
                                                <!-- is_auth es una var que esta mas abajo -->
        <button v-if="is_auth">Cuenta</button>
        <button v-if="is_auth">Cerrar sesión</button>

        <button v-if="!is_auth" v-on:click="loadLogIn">Iniciar sesión</button>  <!-- v-on = listener -->
        <button v-if="!is_auth" v-on:click="loadSignUp">Registrarse</button> 
      </nav>
    </div>

    <div class="main-component">
      <router-view
        v-on:completedLogIn="completedLogIn"
        v-on:completedSignUp="completedSignUp"
      >
      <!-- carga el componente que redirecciona el router -->
      <!-- si se compelta la funcion -> cargue -->
      <!-- Carga sin necesidad de cambiar el endpoint en el url -->
      </router-view>
    </div>

    <footer>
      <div class="footer">
        <h2>MisionTic 2022</h2>
      </div>
    </footer>
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

    data : function(){    //data que cargar con la pagina o componente
      return{
        is_auth: false,
      }
    },

    components:{

    },

    methods: {             //funciones js

      verifyAuth: function(){
        if(this.is_auth == false){
          this.$router.push({name: "LogIn"});
        }
      }, 

      loadLogIn: function(){
        this.$router.push({name: "LogIn"});        //renderiza el componente logIn de router
      },

      loadSignUp: function(){
        this.$router.push({name: "SignUp"});
      },

      completedLogIn: function(data){

      },

      completedSignUp: function(data){

      },
    },

    created: function(){        //se carga con la pag o componente
      this.verifyAuth();
    }
  }
</script>

<style>
  *{
    box-sizing: border-box;
  }

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

  .header nav{
    height: 100%;
    width: 20%;
    display: flex;
    justify-content: space-around;
    align-items: center;
    font-size: 20px;
  }

  .header nav button{
    color: #e5e7e9;
    background: #283747;
    border: 1px solid #e5e7e9;
    border-radius: 5px;
    padding: 10px 20px;
  }

  .header nav button:hover{
    color: #283747;
    background: #e5e7e9;
  }

  .main-component{
    height: 75vh;
    margin: 0;
    padding: 0;
    background: #fdfefe;
  }

  .footer{
    margin: 0;
    padding: 0;
    width: 100%;
    height: 10vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background: #283747;
  }

  .footer h2{
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fdfefe;
  }
</style>
