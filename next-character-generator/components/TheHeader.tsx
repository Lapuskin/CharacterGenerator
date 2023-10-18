import Link from "next/link";
import styles from "../styles/header.module.css"


const TheHeader = () => {

    const hide_or_show_menu = () =>{
        const x: HTMLDivElement = document.getElementById("myTopnav") as HTMLDivElement;
            if (x.className === "topnav") {
                x.className += " responsive";
            } else {
                x.className = "topnav";
            }
    }

    return (
        <header>
            <ul className={styles.header}>
                <li className={styles.logo_block}>
                    <div className={styles.logo}>DungeonGen</div> 
                    <div className={styles.dash}>|</div>
                </li>
                {/* <li><Link href="/" >HOME</Link></li> */}
                <li><Link href="/character-generator">CHARACTER GENERATOR</Link></li>
                {/* <li><Link href="/about">ABOUT</Link></li> */}
            </ul>
        </header>
    );
};

export {TheHeader};