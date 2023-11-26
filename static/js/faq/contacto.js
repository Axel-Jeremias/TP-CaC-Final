import * as Vue from "https://unpkg.com/vue@3/dist/vue.esm-browser.js";
import { contactoCore } from "./contactoCore.Vue.js";

const { createApp } = Vue;

const mainApp = createApp(contactoCore);

mainApp.mount("#vue-app");