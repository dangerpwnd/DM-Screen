import React, {Component} from "react";
import axios from "axios";
import CharImg from "../../components/player/char_img";
import CharMain from "../../components/player/char_main";
import CharAttr from "../../components/player/char_attr";
import CharHp from "../../components/player/char_hp";
import CharDeathSave from "../../components/player/char_deathsave";
import CharModifier from "../../components/player/char_modifier";
import CharSkill from "../../components/player/char_skill";
import CharAttack from "../../components/player/char_attack";
import CharFeat from "../../components/player/char_feat";
import CharEquip from "../../components/player/char_equip";
import CharCoin from "../../components/player/char_coin";
import Characteristics from "../../components/player/characteristics";
import CharNotes from "../../components/player/char_notes";

class PlayerDetail extends Component {
    constructor (props){
        super(props);
        this.state = {
            ac: {
                base: 10,
                nat: 2,
                dex: 2,
                armor: 4,
                magic: 1
            },
            attr: {
                str: 10,
                dex: 10,
                con: 10,
                int: 10,
                wis: 10,
                cha: 10
            },
            hp: {
                current: 1,
                max: 1
            },
            char_class: {
                class_name: "Barbarian",
                level: 1,
                class_speed: "30 ft",
                prof_bonus: 2,
                hit_dice: "d12"
    
            },
            char_name: {
                name : "Bartos Donadarion"
            },
            skill: {
                acrobatics: 0,
                animal: 0,
                arcana: 0,
                athletics: 0,
                deception: 0,
                history: 0,
                insight: 0,
                intimidation: 0,
                investigation: 0,
                medicine: 0,
                nature: 0,
                perception: 0,
                performance: 0,
                persuasion: 0,
                religion: 0,
                sleight: 0,
                stealth: 0,
                survival: 0
            }
        }
    }

    componentDidMount() {
        axios.get('https://localhost:')
            .then(response => {
                console.log(response);
                this.setState({skill: response.data})
            });
    }

    render() {
        return(
            <div>
                <div className="playerDetailGrid">
                    <CharImg />
                    <CharMain 
                        ac={this.state.ac}
                        char_class={this.state.char_class}
                        />
                    <CharAttr attr={this.state.attr}/>
                    <CharHp hp={this.state.hp}/>
                    <CharDeathSave />
                    <CharModifier attr_mod={this.state.attr_mod}/>
                    <CharSkill skill={this.state.skill}/>
                    <CharAttack />
                    <CharFeat />
                    <CharEquip />
                    <CharCoin />
                    <Characteristics />
                    <CharNotes />
                </div>
            </div>
        )
    }
}

export default PlayerDetail;
