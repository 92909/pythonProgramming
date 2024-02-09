// program to find the volume of a cylinder
#include <stdio.h>
float calculateVolume(float radius, float height) {
    const float PI = 3.142;
    float volume = PI * radius * radius * height;
    return volume;
}

int main() {
    float radius, height;

    printf("Enter the radius of the cylinder: ");
    scanf("%f", &radius);

    printf("Enter the height of the cylinder: ");
    scanf("%f", &height);

    float volume = calculateVolume(radius, height);

    printf("The volume of the cylinder is: %.2f\n", volume);

    return 0;
}
