def color_html(color_array):
    color_array = color_array.__str__().split("/")
    color = ""
    for p in color_array:
        color += '<span style="background: {0}" data-toggle="tooltip" data-placement="top" class="box" title ="{0}" > </span>'.format(
            p)
    return color