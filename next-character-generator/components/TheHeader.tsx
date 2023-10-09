import Link from "next/link";


const TheHeader = () => {
    return (
        <header>
            <ul>
            <li><div className="logo">DungeonGen |</div></li>
            <li><Link href="/" >HOME</Link></li>
            <li><Link href="/character-generator">CHARACTER GENERATOR</Link></li>
            <li><Link href="/about">ABOUT</Link></li>
            </ul>
        </header>
    );
};

export {TheHeader};