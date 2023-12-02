import { GridPeliculas } from './gridPelicula.Component.js';

export const CarteleraCore = {
    data: function() {
        return {
            apiPeliculasURL: "https://api.themoviedb.org/3/movie/now_playing?language=es-AR&page=1&api_key=1c4ec8a5b3ce6775aa3d82f650ab9fa8",
            peliculas: [],
            options: {
                method: "GET",
                headers: {
                    accept: "application/json",
                },
            }
        }
    },
    components: {
        GridPeliculas: GridPeliculas
    },
    async created() {
        if (!sessionStorage.hasOwnProperty("peliculas")) {
            console.log("No hay cache de peliculas");

            const response = await fetch(this.apiPeliculasURL, this.options);
            const jsonResponse = await response.json();
            this.peliculas = jsonResponse.results;

            this.peliculas.sort(function (a, b) {
                return b.vote_count - a.vote_count;
            });

            this.peliculas.forEach((pelicula) => this.formatearPelicula(pelicula))

            sessionStorage.setItem("peliculas", JSON.stringify(this.peliculas));
        } else {
            console.log("Cache de peliculas encontrado");
            this.peliculas = JSON.parse(sessionStorage.getItem("peliculas"));
        }
    },
    methods: {
        formatearPelicula: function(pelicula) {
            // Pasamos de YYYY-MM-DD a DD/MM/YY
            let fecha = pelicula.release_date.split("-").reverse();
            fecha[2] = fecha[2].substring(2);
            pelicula.fecha = fecha.join("/");

            // Si el titulo contiene un texto en parentesis al final, lo sacamos
            // Usado para titulos que tienen el formato "Titulo en español (en ingles)"
            pelicula.title = pelicula.title.replace(/ *\([^)]*\)$/g, "");

            // The Movie Database cambió el rating que devuelve a uno con 3 decimales
            // Para nuestro uso, lo convertimos a uno con 1 decimal como era antes
            pelicula.rating = pelicula.vote_average.toFixed(1);

            pelicula.poster_path = 'https://image.tmdb.org/t/p/w500/' + pelicula.poster_path;

            return pelicula;
        }
    }
};