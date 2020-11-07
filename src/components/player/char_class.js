import React from "react";

const charClass = (props) => {

    return(
        <div>
            <div className="border playerFlexRow">
                <h2>{props.class_name}</h2>
                <h2>{props.level}</h2>
            </div>
        </div>
    )
};

export default charClass;