import React from "react";

const charSpeed = (props) => {
    return(
        <div>
            <div className="border playerFlexRow">
                <h3>Speed: {props.class_speed}</h3>
                <h3>Initiative: 2</h3>
            </div>
        </div>
    )
};

export default charSpeed;