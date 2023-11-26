import * as Vue from "https://unpkg.com/vue@3/dist/vue.esm-browser.js";
import { CarteleraCore } from "./CarteleraCore.Vue.js";

const { createApp } = Vue;

const mainApp = createApp(CarteleraCore);

mainApp.mount("#vue-app");