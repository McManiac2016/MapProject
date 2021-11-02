
import osmnx as ox
import networkx as nx

def generate(center):
    city = ox.graph_from_point(center, dist=2500, dist_type="bbox",
                            network_type="all", simplify=True)

    u = []
    v = []
    key = []
    data = []
    for uu, vv, kkey, ddata in city.edges(keys=True, data=True):
        u.append(uu)
        v.append(vv)
        key.append(kkey)
        data.append(ddata)
    print("Unpacked streets")

    roadColors = []
    roadWidths = []

    for item in data:
            color = "#494949"
            linewidth =0.5
            roadColors.append(color)
            roadWidths.append(linewidth)

    print("Colorated")

    water = ox.graph_from_point(center, dist=2500, dist_type="bbox", network_type='all',
                                 simplify=True, retain_all=True, truncate_by_edge=False,
                                 clean_periphery=False, custom_filter='["waterway"~"river"]')

    u = []
    v = []
    key = []
    data2 = []
    for uu, vv, kkey, ddata in water.edges(keys=True, data=True):
        u.append(uu)
        v.append(vv)
        key.append(kkey)
        data2.append(ddata)
    print("Unpacked waters")

    for item in data2:
            color = "#0086cf"
            linewidth = 2
            roadColors.append(color)
            roadWidths.append(linewidth)

    G = nx.compose(city, water)
    fig, ax = ox.plot_graph(G, node_size=0, figsize=(27, 40),
                            dpi=300, bgcolor="#F2F2F2",
                            save=False, edge_color=roadColors,
                            edge_linewidth=roadWidths, edge_alpha=1,show=False,close=False)
    fig.savefig("HartaGenerata.png", dpi=300, bbox_inches='tight', format="png",
                 facecolor=fig.get_facecolor(), transparent=False)