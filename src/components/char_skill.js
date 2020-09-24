import React from "react";

const charSkill = (props) => {
    return(
        <div className="playerStatGrid">
            <div className="border">
                <h3>Acrobatics: {props.skill.acrobatics}</h3>
                <h3>Animal Handling: {props.skill.animal}</h3>
                <h3>Arcana: {props.skill.arcana}</h3>
                <h3>Athletics: {props.skill.athletics}</h3>
                <h3>Deception: {props.skill.deception}</h3>
                <h3>History: {props.skill.history}</h3>
                <h3>Insight: {props.skill.insight}</h3>
                <h3>Intimidation: {props.skill.intimidation}</h3>
                <h3>Investigation: {props.skill.investigation}</h3>
                <h3>Medicine: {props.skill.medicine}</h3>
                <h3>Nature: {props.skill.nature}</h3>
                <h3>Perception: {props.skill.perception}</h3>
                <h3>Performance: {props.skill.performance}</h3>
                <h3>Persuasion: {props.skill.persuasion}</h3>
                <h3>Religion: {props.skill.religion}</h3>
                <h3>Sleight of Hand: {props.skill.sleight}</h3>
                <h3>Stealth: {props.skill.stealth}</h3>
                <h3>Survival: {props.skill.survival}</h3>
            </div>
        </div>
    )
};

export default charSkill;