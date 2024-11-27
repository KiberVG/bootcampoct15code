import "./Navbar.css"

export default function Navbar() {
    return (
        <nav>
            <div id="logo">
                <h1>Notes App</h1>
            </div>
            <div id="link-list">
                <ul>
                    <li>Home</li>
                    <li>About</li>
                    <li>Contact</li> 
                </ul>
            </div>
        </nav>
    );
}