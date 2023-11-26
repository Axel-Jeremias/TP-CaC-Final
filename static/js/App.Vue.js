import { Novedad } from './components/novedad.Component.js';
import { Navbar } from './components/navbar.Component.js';
import { Footer } from './components/footer.Component.js';

export const mainCore = {
    data: function() {
        return {
            numeroSlide: 1,
            novedades: [],
            jsonData: '/static/js/data.json',
            hoveringSlide: false,
            nuevaNovedad: {},
            trailers: []
        }
    },
    components: {
        Novedad: Novedad,
        Navbar: Navbar,
        VueFooter: Footer
    },
    async created() {
        const response = await fetch(this.jsonData);
        const json = await response.json();
        this.novedades = json["novedades"];
        this.trailers = json["trailers"];
        this.nuevaNovedad = this.novedades[0];

        setInterval(this.loopNovedad, 8000);
    },
    methods: {
        loopNovedad: function() {
            if (!this.hoveringSlide) {
                if (this.numeroSlide >= this.novedades.length) {
                    this.numeroSlide = 1;
                } else {
                    this.numeroSlide++;
                }

                this.nuevaNovedad = this.novedades[this.numeroSlide - 1];
            }
        }
    }
};