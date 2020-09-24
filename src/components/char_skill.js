import React from "react";

const charSkill = (props) => {
    return(
        <div className="playerStatGrid">
            <div className="border">
                <h3>Acrobatics: {props.skill.Acrobatics}</h3>
                <h3>Animal Handling: {props.skill.Animal}</h3>
                <h3>Arcana: {props.skill.Arcana}</h3>
                <h3>Athletics: {props.skill.Athletics}</h3>
                <h3>Deception: {props.skill.Deception}</h3>
                <h3>History: {props.skill.History}</h3>
                <h3>Insight: {props.skill.Insight}</h3>
                <h3>Intimidation: {props.skill.Intimidation}</h3>
                <h3>Investigation: {props.skill.Investigation}</h3>
                <h3>Medicine: {props.skill.Medicine}</h3>
                <h3>Nature: {props.skill.Nature}</h3>
                <h3>Perception: {props.skill.Perception}</h3>
                <h3>Performance: {props.skill.Performance}</h3>
                <h3>Persuasion: {props.skill.Persuasion}</h3>
                <h3>Religion: {props.skill.Religion}</h3>
                <h3>Sleight of Hand: {props.skill.Sleight}</h3>
                <h3>Stealth: {props.skill.Stealth}</h3>
                <h3>Survival: {props.skill.Survival}</h3>
            </div>
        </div>
    )
};

export default charSkill;