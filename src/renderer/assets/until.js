const windowToCanvas = (canvas, x, y) => {
    let rect = canvas.getBoundingClientRect()
    return {
        x: x - rect.left * (canvas.width/rect.width),
        y: y - rect.top * (canvas.height/rect.height)
    }
}
 
