import WazeRouteCalculator
import logging

logger = logging.getLogger('WazeRouteCalculator.WazeRouteCalculator')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
logger.addHandler(handler)


def estimador_ruta(dir_ini,dir_fin,ciudad_ini='Madrid',ciudad_fin='Madrid',pais_ini='Spain', pais_fin='Spain', region ='EU'):
    
    from_address=', '.join([dir_ini, ciudad_ini, pais_ini])
    to_address=', '.join([dir_fin, ciudad_fin, pais_fin])
    route = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address, region)
    ruta = route.get_route();
    info = route.calc_route_info();
    avg_speed = 60 * info[1] / info[0]
    return(info[0], info[1], avg_speed)

