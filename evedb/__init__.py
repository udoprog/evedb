#
class dbo(object):
  pass;

def create_source_engine(cs):
  from sqlalchemy import create_engine
  return create_engine(cs);

def create_target_engine(cs):
  from sqlalchemy import create_engine
  return create_engine(cs);

def map_tables(engine, create_all=False):
  from sqlalchemy import *
  
  o = dbo();
  metadata = MetaData();
  
  o.engine = engine;
  metadata.bind = engine;
  
  o.mapSolarSystems = Table('mapSolarSystems', metadata,
    Column('solarSystemID', Integer, primary_key=True),
    Column('constellationID', Integer),
    Column('regionID', Integer),
    Column('solarSystemName', String(100)),
  );
  
  o.mapSolarSystemJumps = Table('mapSolarSystemJumps', metadata,
    Column('fromSolarSystemID', Integer, primary_key=True),
    Column('toSolarSystemID', Integer, primary_key=True),
    Column('fromConstellationID', Integer),
    Column('toConstellationID', Integer),
    Column('fromRegionID', Integer),
    Column('toRegionID', Integer),
  );
  
  o.mapConstellations = Table('mapConstellations', metadata,
    Column('constellationID', Integer, primary_key=True),
    Column('constellationName', String(100)),
  );
  
  o.mapRegions = Table('mapRegions', metadata,
    Column('regionID', Integer, primary_key=True),
    Column('regionName', String(100)),
  );
  
  if create_all:
    metadata.create_all();
  
  return o;

def copy_table(source, target, table_name):
  s_conn = source.engine.connect();
  t_conn = target.engine.connect();
  
  s_table = getattr(source, table_name)
  t_table = getattr(target, table_name)

  data=list(s_conn.execute(s_table.select()));
  t_conn.execute(t_table.insert(), data);

def entrypoint():
  import sys
  
  if len(sys.argv) != 3:
    print("Usage: evedb <source> <target>")
    sys.exit(1);
  
  s_cs = sys.argv[1]
  t_cs = sys.argv[2]
  
  print("Connecting to databases");
  print("   connecting to source database");
  source = map_tables(create_source_engine(s_cs));
  print("   mapping target database");
  target = map_tables(create_target_engine(t_cs), True);

  print("Copying Data");
  print("   copying Regions");
  copy_table(source, target, 'mapRegions')
  print("   copying Constellations");
  copy_table(source, target, 'mapConstellations')
  print("   copying SolarSystems");
  copy_table(source, target, 'mapSolarSystems')
  print("   copying SolarSystemJumps");
  copy_table(source, target, 'mapSolarSystemJumps')

if __name__ == "__main__":
  entrypoint();
