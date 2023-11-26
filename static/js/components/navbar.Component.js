import { ListPages } from "./listPages.Component.js";

export const Navbar = {
    data: function() {
        return {
            logoPath: "/static/img/logo/logo-mf.png"
        }
    },
    components: {
        ListPages: ListPages
    },
    template: `
        <header id="header">
            <div id="navbar">
                <div id="logo-container">
                    <img :src="this.logoPath" id="logo" alt="MasterFrame logo">
                </div>
                <ul>
                    <ListPages></ListPages>
                </ul>
            </div>
        </header>
    `,
};