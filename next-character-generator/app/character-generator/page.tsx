"use client"
import TheCharacter from "@/components/TheCharacter";
import TheParagraph from "@/components/TheParagraph";
import TheForm from "@/components/TheForm";
import styles from "../../styles/generator-page.module.css"
import TheButton from "@/components/TheButton";
import { useState , ChangeEvent} from "react";
import { Character } from "../utils/json_character";

export default function CharacterGenerator() {
    const [formData, setFormData] = useState<Record<string, string>>({
        stateRace: '',
        stateClass: '',
        stateType: '', 
        stateSpecialities: '',
    })

    const [response, setResponse] = useState<Character> ()

    const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    console.log(formData)
    var url ='http://127.0.0.1:8000/api/v1/character?'
    for (var key in formData){
        console.log(key)
        if (formData[key] !=''){
            url += key + '=' + formData[key] + '&'
        }
    }
    url = url.slice(0, -1);
        
    // Отправка данных на сервер
    fetch(url, {
        method: 'GET',
        headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        },
        })
        .then(response => response.json())
        .then(data => {
        console.log(data)
        setResponse(data)
        })
        .catch(error => {
        alert("Что-то пошло не так. Приносим свои извинения.\n" + error)
        });
        
    };
    
    const handleFormChange = (event:ChangeEvent<HTMLInputElement>) => {
        const { name, value } = event.target;
        setFormData((prevData) => ({
          ...prevData,
          [name]: value,
        }));
    };
   

    return (<div>
        <TheParagraph title={'ГЕНЕРАТОР ПЕРСОНАЖЕЙ МАСТЕРА'} text1 = {'Данный генератор создает уникальных персонажей, определяя их тип личности, расу, характеристики и особенности.\n\nМы понимаем, что создание персонажей может быть сложным и занимать много времени. Поэтому наш генератор поможет вам быстро получить интересного персонажа для ваших игровых сессий. Вы сможете использовать сгенерированные персонажи как вдохновение для своих собственных созданий или прямо внедрять их в свою игру. \nНе упускайте возможность использовать наш генератор случайных персонажей для мастера игры в D&D и получите уникального персонажа уже сегодня!'} />
        <form onSubmit={handleSubmit}>
            <div className={styles.form_block}>
                <TheForm params={['Раса', 'Орк', 'Хуман']} 
                change={handleFormChange} 
                name='stateRace'
                />
                <TheForm params={['Класс', 'Плут', 'Паладин']} 
                change={handleFormChange}
                name="stateClass"
                />
                <TheForm params={['Тип личности', 'ENTP', 'ENTJ']} 
                change={handleFormChange}
                name="stateType"
                />
                <TheForm params={['Особенности', 'Кривой', 'Косой']} 
                change={handleFormChange}
                name="stateSpecialities"
                />
            </div> 
            <div className={styles.generate_position}><TheButton text={'Сгенерировать персонажа'} /> </div>    
        </form>  
        {response &&  <TheCharacter params={response}/> }
      </div>
      );
  };
  