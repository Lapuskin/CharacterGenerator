"use client"
import styles from "../styles/menu.module.css"
import { useState } from "react";
import TheBurger from "./TheBurger";


const TheMenu: React.FC = () => {
    const [open, setOpen] = useState<boolean>(false);
    const close = () =>{ 
        setOpen(false)
    };
    
    return (<div className={styles.sidebar}>
                {open && (
                        <div className={styles.back}>
                            <a onClick={close}>Link 1</a>   
                            <a onClick={close}>Link 2</a>   
                            <a onClick={close}>Link 3</a>   
                        </div>
                )}
        <TheBurger open={open} setOpen={setOpen}/>
        </div>
    );
};

export default TheMenu;