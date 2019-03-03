<template>
  <div>
    <h3>雷达</h3>
    <div id="plot">
      <!-- <svg id="svg" viewBox="0,0,500,500" width="100%" height="100%">
            <g :transform="transform_str">
                <line v-for="l in lines" :x1="l[0]" :y1="l[1]" :x2="l[2]" :y2="l[3]" />
            </g>
            <g :transform="transform_str">
                <polyline v-for="l in polylines" :points="l"></polyline>
            </g>
      </svg>-->
      <canvas id="canvas" width="800" height="600" @mouseenter="mouseenter" @mouseleave="mouseleave" @mousedown="mousedown($event)" @mousemove.prevent='mousemove($event)' @mouseup='mouseup($event)' @mousewheel='mousewheel($event)'></canvas>
    </div>
  </div>
</template>


<script>
// window.plotshow = function () {
//   console.log('SHOW')
// }

var shaderlib = {
  points: {
    vert: `
    attribute vec3 position;
    varying float heat;
    uniform mat3 transform;
    void main() {
       vec3 p = transform * vec3(position.xy, 1.0);
       gl_Position = vec4(p.xy,0.0, 1.0);
       heat = float(position.z);
    }    
    `,

    frag: `
    precision mediump float;
    varying float heat;
    void main() {
      gl_FragColor = vec4(vec3(heat, 0.4-heat, 1.0 - heat), heat+0.4);
    }
    `
  },

  axisLines: {
    vert: `
    attribute vec2 position;
    uniform mat3 transform;
    void main(){
      vec3 p = transform * vec3(position.xy, 1.0);
      gl_Position = vec4(p.xy,0.0, 1.0);
    }
    `,

    frag: `
    precision mediump float;
    void main() {
      gl_FragColor = vec4(0.0,0.5,0.0,1.0);
    }
    `
  }
}

var createProgram = function (gl, vs, fs) {
  var vertShader = gl.createShader(gl.VERTEX_SHADER)
  var fragShader = gl.createShader(gl.FRAGMENT_SHADER)
  // var geomShader = gl.createShader(gl.GEOMETRY_SHADER)
  gl.shaderSource(vertShader, vs)
  gl.shaderSource(fragShader, fs)
  // gl.shaderSource(geomShader, geom)
  gl.compileShader(vertShader)
  gl.compileShader(fragShader)
  // gl.compileShader(geomShader)

  var program = gl.createProgram()
  gl.attachShader(program, vertShader)
  gl.attachShader(program, fragShader)
  // gl.attachShader(program, geomShader)
  gl.linkProgram(program)
  return program
}

var pointsVertexGen = function (points) {
  var result = []
  var rad = 0.02
  for (var i in points) {
    result = result.concat([points[i][0] - rad, points[i][1] - rad, points[i][2]])
    result = result.concat([points[i][0] + rad, points[i][1] - rad, points[i][2]])
    result = result.concat([points[i][0] - rad, points[i][1] + rad, points[i][2]])

    result = result.concat([points[i][0] - rad, points[i][1] + rad, points[i][2]])
    result = result.concat([points[i][0] + rad, points[i][1] - rad, points[i][2]])
    result = result.concat([points[i][0] + rad, points[i][1] + rad, points[i][2]])
  }
  // console.log(result)
  // console.log(result)
  return result
}

export default {
  data () {
    return {
      points: [],

      zoom: 1.0,
      zoomLevel: 0,
      position: [0, -0.5]

    }
  },

  computed: {},

  methods: {
    draw () {
      var gl = this.gl
      gl.bindBuffer(gl.ARRAY_BUFFER, this.bufferPoints)
      gl.bufferData(
        gl.ARRAY_BUFFER,
        // new Float32Array([-1, -1, 0, 1, -1, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
        new Float32Array(pointsVertexGen(this.points)),
        gl.STATIC_DRAW
      )
      var positionLocation = gl.getAttribLocation(this.programPoints, 'position')
      var transformLocation = gl.getUniformLocation(this.programPoints, 'transform')

      var positionLocationAxis = gl.getAttribLocation(this.programAxis, 'position')
      var transformLocationAxis = gl.getUniformLocation(this.programAxis, 'transform')

      var transformMatrix =
        [ 0.75 * this.zoom, 0, 0,
          0, 1 * this.zoom, 0,
          0.75 * this.position[0], this.position[1], 1]
      if (this.points.length > 0) {
        gl.useProgram(this.programPoints)
        gl.uniformMatrix3fv(transformLocation, false, transformMatrix)

        gl.enableVertexAttribArray(positionLocation)
        gl.vertexAttribPointer(positionLocation, 3, gl.FLOAT, false, 0, 0)
        // draw
        gl.drawArrays(gl.TRIANGLES, 0, this.points.length * 6)
      }
      gl.bindBuffer(gl.ARRAY_BUFFER, this.bufferAxis)

      gl.useProgram(this.programAxis)
      gl.uniformMatrix3fv(transformLocationAxis, false, transformMatrix)
      gl.enableVertexAttribArray(positionLocationAxis)
      gl.vertexAttribPointer(positionLocationAxis, 2, gl.FLOAT, false, 0, 0)
      gl.drawArrays(gl.LINES, 0, 128)
    },

    mousedown: function (event) {
      this.last_pos = {x: event.x, y: event.y}
      this.is_moving = true
      // this.old_position = this.position
    },
    mousemove: function (event) {
      if (this.is_moving) {
        // event.target.style.left = endx + 'px'
        // event.target.style.top = endy + 'px'
        // console.log([event.x, event.y])
        var curPos = {x: event.x, y: event.y}
        this.position[0] += (curPos.x - this.last_pos.x) * 0.005
        this.position[1] -= (curPos.y - this.last_pos.y) * 0.005
        this.last_pos = curPos

        // this.position[0] = this.old_position[0] + (this.down_pos.x - event.x) * 0.0001
        // this.position[1] = this.old_position[1] + (this.down_pos.y - event.y) * 0.0001
        // this.draw()
      }
    },
    mouseup: function (e) {
      this.is_moving = false
    },
    mousewheel: function (event) {
      if (event.deltaY > 0) {
        this.zoomLevel += 1
      } else {
        this.zoomLevel -= 1
      }
      this.zoom = Math.pow(2, this.zoomLevel / 5)
      // console.log(event)
      // console.log(this.zoom)
    },

    mouseenter: function () {
      // console.log('ENTER')
      window.document.body.style.overflow = 'hidden'
    },
    mouseleave: function () {
      // console.log('LEAVE')
      window.document.body.style.overflow = ''
    }

  },
  created () {
    window.parsed_points = this.points
  },
  mounted () {
    var canvas = document.getElementById('canvas')
    var gl = canvas.getContext('experimental-webgl')
    this.gl = gl

    var programPoints = createProgram(gl, shaderlib.points.vert, shaderlib.points.frag)
    var programAxis = createProgram(gl, shaderlib.axisLines.vert, shaderlib.axisLines.frag)

    this.programPoints = programPoints
    this.programAxis = programAxis

    var bufferPoints = gl.createBuffer()
    this.bufferPoints = bufferPoints

    var bufferAxis = gl.createBuffer()
    this.bufferAxis = bufferAxis

    var axisVertex = [
      -100, 0, 100, 0, 0, -100, 0, 100, -100, 100, 0, 0, 0, 0, 100, 100
    ]

    for (var i = 1; i <= 50; i++) {
      axisVertex = axisVertex.concat([0, i / 5, i / 5, i / 5])
    }

    for (i = 1; i <= 10; i++) {
      axisVertex = axisVertex.concat([0, i, -i, i])
    }
    // var bufferAxis = gl.createBuffer()

    gl.bindBuffer(gl.ARRAY_BUFFER, this.bufferAxis)
    gl.bufferData(gl.ARRAY_BUFFER,
      // new Float32Array([-1, -1, 0, 1, -1, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
      new Float32Array(axisVertex),
      gl.STATIC_DRAW)

    window.setInterval(() => {
      this.draw()
      for (var i in this.points) {
        this.points[i][2] -= 0.001
        if (this.points[i][2] < 0) {
          this.points[i][2] = 0
        }
      }
    }, 10)

    window.eventBus.$on('dot', (arg) => {
      this.points.push([arg.x, arg.y, 1])
      console.log('message on!' + this.points)
    })

    // gl.useProgram(programPoints)

    // var bufferPoints = gl.createBuffer()
    // this.bufferPoints = bufferPoints
    // gl.bindBuffer(gl.ARRAY_BUFFER, bufferPoints)

    // var points = [
    //   [-0.6, 0.6, 0.0],
    //   [-0.54, 0.6426, 0.05],
    //   [-0.48, 0.6528, 0.1],
    //   [-0.42, 0.6342, 0.15],
    //   [-0.36, 0.5904, 0.2],
    //   [-0.3, 0.525, 0.25],
    //   [-0.24, 0.4416, 0.3],
    //   [-0.18, 0.3438, 0.35],
    //   [-0.12, 0.2352, 0.4],
    //   [-0.06, 0.1194, 0.45],
    //   [-0.0, 0.0, 0.5],
    //   [0.06, -0.1194, 0.55],
    //   [0.12, -0.2352, 0.6],
    //   [0.18, -0.3438, 0.65],
    //   [0.24, -0.4416, 0.7],
    //   [0.3, -0.525, 0.75],
    //   [0.36, -0.5904, 0.8],
    //   [0.42, -0.6342, 0.85],
    //   [0.48, -0.6528, 0.9],
    //   [0.54, -0.6426, 0.95],
    //   [0.6, -0.6, 1.0]]
    // // var points = [[-0.5, -0.5, 1.0], [-0.2, 0.0, 1], [0.0, 0.0, 1.0]]

    // this.gl = gl

    // gl.bufferData(
    //   gl.ARRAY_BUFFER,
    //   // new Float32Array([-1, -1, 0, 1, -1, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    //   new Float32Array(pointsVertexGen(points)),
    //   gl.STATIC_DRAW
    // )
    // var positionLocation = gl.getAttribLocation(programPoints, 'position')
    // var transformLocation = gl.getUniformLocation(programPoints, 'transform')

    // var positionLocationAxis = gl.getAttribLocation(programAxis, 'position')
    // var transformLocationAxis = gl.getUniformLocation(programAxis, 'transform')

    // var zoom = 1.0
    // var pos = [0, -0.5]
    // var transformMatrix =
    // [ 0.75 * zoom, 0, 0,
    //   0, 1 * zoom, 0,
    //   pos[0], pos[1], 1]

    // gl.uniformMatrix3fv(transformLocation, false, transformMatrix)

    // gl.enableVertexAttribArray(positionLocation)
    // gl.vertexAttribPointer(positionLocation, 3, gl.FLOAT, false, 0, 0)
    // // draw
    // gl.drawArrays(gl.TRIANGLES, 0, 126)

    // gl.useProgram(programAxis)
    // var axisVertex = [
    //   -100, 0, 100, 0, 0, -100, 0, 100, -100, 100, 0, 0, 0, 0, 100, 100
    // ]

    // var bufferAxis = gl.createBuffer()
    // this.bufferAxis = bufferAxis

    // gl.bindBuffer(gl.ARRAY_BUFFER, bufferAxis)
    // gl.bufferData(gl.ARRAY_BUFFER,
    //   // new Float32Array([-1, -1, 0, 1, -1, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    //   new Float32Array(axisVertex),
    //   gl.STATIC_DRAW)

    // gl.uniformMatrix3fv(transformLocationAxis, false, transformMatrix)
    // gl.enableVertexAttribArray(positionLocationAxis)
    // gl.vertexAttribPointer(positionLocationAxis, 2, gl.FLOAT, false, 0, 0)
    // gl.drawArrays(gl.LINES, 0, 8)
  }
}
</script>

<style>
#canvas {
  width: 100%;
}
</style>


