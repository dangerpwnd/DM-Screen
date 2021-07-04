import React from "react";

const charSkill = (props) => {

    const { acrobatics, animal, arcana, athletics, deception, 
                history, insight, intimidation, investigation, medicine, 
                nature, perception, performance, persuasion,
                religion, sleight, stealth, survival    
            } = props;

    return(
        <div className="playerStatGrid">
            <div className="border">
                <h3>Acrobatics: {acrobatics}</h3>
                <h3>Animal Handling: {animal}</h3>
                <h3>Arcana: {arcana}</h3>
                <h3>Athletics: {athletics}</h3>
                <h3>Deception: {deception}</h3>
                <h3>History: {history}</h3>
                <h3>Insight: {insight}</h3>
                <h3>Intimidation: {intimidation}</h3>
                <h3>Investigation: {investigation}</h3>
                <h3>Medicine: {medicine}</h3>
                <h3>Nature: {nature}</h3>
                <h3>Perception: {perception}</h3>
                <h3>Performance: {performance}</h3>
                <h3>Persuasion: {persuasion}</h3>
                <h3>Religion: {religion}</h3>
                <h3>Sleight of Hand: {sleight}</h3>
                <h3>Stealth: {stealth}</h3>
                <h3>Survival: {survival}</h3>
            </div>
        </div>
    )
};

export default charSkill;