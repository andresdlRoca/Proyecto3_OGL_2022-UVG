vertex_shader ='''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texcoords;
layout (location = 2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float time;

out vec2 UVs;
out vec3 norms;
out vec3 pos;

void main()
{
    //
    //pos = (modelMatrix * vec4(position + normals* sin(time * 3)/10, 1.0)).xyz;
    //gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position + normals * sin(time * 3)/10 , 1.0);
    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position, 1.0);
    UVs = texcoords;
    norms = normals;
    pos = (modelMatrix * vec4(position, 1.0)).xyz;

}
'''

fragment_shader ='''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;

uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight -pos));
    fragColor = texture(tex, UVs) * intensity;

}
'''

toon_shader = '''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;

uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight -pos));

    if(intensity < 0.2){
        intensity = 0.1;
    }
    else if(intensity < 0.5){
        intensity = 0.4;
    }
    else if(intensity < 0.8) {
        intensity = 0.7;
    }
    else if(intensity <= 1){
        intensity = 1;
    }

    fragColor = texture(tex, UVs) * intensity;
}
'''

glow_shader = '''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;

uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight -pos));
    float glowAmount = 1 - intensity;

    if (glowAmount <= 0) {
        glowAmount = 0;
    }
    //yellow = 1,1,0 RGB

    vec4 textr = texture(tex, UVs);
    float glowValue = 1 * glowAmount;

    if (glowValue > 1) {
        glowValue = 1;
    }
    fragColor = textr + vec4(glowValue,glowValue,0,1) * intensity;

}
'''

pinkJelly_shader = '''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;

uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight -pos));

    vec4 textr = texture(tex, UVs);

    fragColor = textr + vec4(1,0,1,1) * intensity;

}
'''

pulse_vertex_shader ='''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texcoords;
layout (location = 2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float time;

out vec2 UVs;
out vec3 norms;
out vec3 pos;

void main()
{
    
    //pos = (modelMatrix * vec4(position + normals * sin(time * 3)/10), 1.0)).xyz;
    //gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position + normals * sin(time * 3)/10) , 1.0);
    //gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position + normals * sin(time * 3)/10 , 1.0);
    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position, 1.0);
    UVs = texcoords;
    norms = normals;
    pos = (modelMatrix * vec4(position, 1.0)).xyz;

}
'''

pulse_fragment_shader ='''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;

uniform sampler2D tex;
uniform float time;

void main()
{
    float intensity = dot(norms, normalize(pointLight -pos));

    vec4 textr = texture(tex, UVs);

    fragColor = textr + vec4(1*sin(time * 3)/5,0,0.51*sin(time * 3)/5,0) * intensity;

}
'''