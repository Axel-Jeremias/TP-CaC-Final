import * as Vue from "https://unpkg.com/vue@3/dist/vue.esm-browser.js";
import { mainCore } from "./App.Vue.js";

const { createApp } = Vue;

const mainApp = createApp(mainCore);

mainApp.mount("#vue-app");