
import { Character } from "@/app/utils/json_character";
import styles from "../styles/character.module.css";

interface TheCharacterProops {
    params: Character
}

const genModify = (state: number) => { 
    let result = (0.502)*state + -(5.28);
    return Math.round(result);
}; 

const TheCharacter: React.FC<TheCharacterProops> = ({ params }) => {
    return (
        <div>
            <div className={styles.header}>
                {/* {params.personality.first_letter}{params.personality.second_letter}{params.personality.third_letter}{params.personality.fourth_letter} */}
                <h2>{params.name}, </h2>
                <h3><a href={params.race.link} target="_blank">{params.race.name}</a> <a target="_blank" href={params.class.link}>{params.class.name}</a>, в прошлом <a  target="_blank"href={params.background.link}>{params.background.title}</a></h3>
                <div className={styles.stats}>
                    <div className={styles.state}>
                        <span>СИЛ</span>
                        <span>{params.stats.force} ( {genModify(params.stats.force)})</span>
                    </div>
                    <div className={styles.state}>
                        <span>ЛОВ</span>
                        <span>{params.stats.dexterity} ( {genModify(params.stats.dexterity)})</span>
                    </div>
                    <div className={styles.state}>
                        <span>ТЕЛ</span>
                        <span>{params.stats.endurance} ( {genModify(params.stats.endurance)})</span>
                    </div>
                    <div className={styles.state}>
                        <span>ИНТ</span>
                        <span>{params.stats.intelligence} ( {genModify(params.stats.intelligence)})</span>
                    </div>
                    <div className={styles.state}>
                        <span>МДР</span>
                        <span>{params.stats.wisdom} ( {genModify(params.stats.wisdom)})</span>
                    </div>
                    <div className={styles.state}>
                        <span>ХАР</span>
                        <span>{params.stats.charisma} ( {genModify(params.stats.charisma)})</span>
                    </div>
                </div>
            </div>

            <div className={styles.description}>
                <p><strong>Краткое описание:</strong>
                    <span>Про расу: {params.race.description}</span>
                    <span>Про тип личности:</span>
                    <ul>
                        <li>{params.personality.first_letter}</li>
                        <li>{params.personality.second_letter}</li>
                        <li>{params.personality.third_letter}</li>
                        <li>{params.personality.fourth_letter}</li>
                    </ul>
                </p>
                <div>
                    <p><strong>Особенности:</strong> {params.peculiarities.description}</p>
                    <p><strong>Идеал:</strong> {params.ideal.description}</p>
                    <p><strong>Слабость:</strong> {params.weakness.description}</p>
                </div>
            </div>
        </div>
    );
};

export default TheCharacter;